import os
import re
from requests import get
from tabulate import tabulate
import math
from os.path import relpath


resp = get("https://print.niimbot.com/api/hardware/list")
resp.raise_for_status()
model_list = resp.json()["data"]["list"]
for m in model_list:
    m["name"] = re.sub(r"[\s\-]", "_", m["name"]).upper()

model_list.sort(key=lambda m: m["name"])


def transform_model_info(model):
    ppmm_dict = {
        "203": 8,
        "300": 11.81,
    }

    dir_dict = {
        270: "left",
        180: "top",
        90: "left",
        0: "top",
    }

    type_dict = {
        "热转印打印机": "thermal transfer",
        "热敏打印机": "thermal",
        "线号机": "wire marking",
        "电子价签": "electronic price tag",
        "热敏及热转印打印机": "thermal transfer"
    }

    out = {}

    out["name"] = model["name"]
    out["id"] = ", ".join([str(i) for i in model["codes"]])
    out["head_mm"] = model["widthSetEnd"]
    out["head_px"] = math.ceil(model["widthSetEnd"] * ppmm_dict[model["paccuracyName"]])
    out["dpi"] = (
        "**300**" if model["paccuracyName"] == "300" else model["paccuracyName"]
    )
    out["dir"] = dir_dict[model["printDirection"]]
    out["papers"] = model["paperType"]
    out["density"] = f"{model['solubilitySetStart']}-[{model['solubilitySetDefault']}]-{model['solubilitySetEnd']}"
    out["type"] = type_dict[model["modelName"]]
    return out

root = "./docs"

for dir_name, _, files in os.walk(root):
    for file_name in files:
        if not file_name.endswith(".md"):
            continue

        file_path = os.path.join(dir_name, file_name)

        root_rel = relpath(root, dir_name).replace("\\", "/")

        with open(file_path, encoding="utf-8") as f:
            file_contents = f.read()

        if "<!-- BEGIN" not in file_contents:
            continue

        def replace_single_printer_info(match):
            start, printer_name, end = match.groups()
            print("Filling", printer_name, "block in", file_name)

            table = "ERROR"

            model = next(m for m in model_list if m["name"] == printer_name)

            if model is not None:
                info = transform_model_info(model)

                header = ["Parameter", "Value"]
                data = [
                    ["ID", info["id"]],
                    ["DPI", info["dpi"]],
                    [
                        "Printhead size",
                        f"{info['head_mm']}mm ({info['head_px']}px)",
                    ],
                    ["Print direction", info["dir"]],
                    [f"[Paper types]({root_rel}/interfacing/paper-types.md)", info["papers"]],
                    ["Density range", info["density"]],
                    ["Printer type", info["type"]],
                ]
                table = tabulate(data, header, tablefmt="github")
            else:
                print("Model", printer_name, "not found")
            return f"{start}<!-- Auto-generated, do not edit -->\n{table}\n{end}"

        def replace_all_printers_info(match):
            start, end = match.groups()
            print("Filling printers table in", file_name)

            header = [
                "Name",
                "ID",
                "DPI",
                "Printhead size",
                "Print direction",
                f"[Paper types]({root_rel}/interfacing/paper-types.md)",
                "Density range",
                "Printer type",
            ]

            data = []

            for model in model_list:
                info = transform_model_info(model)
                data.append(
                    [
                        info["name"],
                        info["id"],
                        info["dpi"],
                        f"{info['head_mm']}mm ({info['head_px']}px)",
                        info["dir"],
                        info["papers"],
                        info['density'],
                        info['type'],
                    ]
                )

            table = tabulate(data, header, tablefmt="github")

            return f"{start}<!-- Auto-generated, do not edit -->\n{table}\n{end}"

        file_contents = re.sub(
            r"(<!-- BEGIN (\w+) CLOUD_INFO -->\n).*?(<!-- END CLOUD_INFO -->\n)",
            replace_single_printer_info,
            file_contents,
            flags=re.DOTALL,
        )

        file_contents = re.sub(
            r"(<!-- BEGIN CLOUD_PRINTERS_TABLE -->\n).*?(<!-- END CLOUD_PRINTERS_TABLE -->\n)",
            replace_all_printers_info,
            file_contents,
            flags=re.DOTALL,
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_contents)
