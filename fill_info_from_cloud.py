import os
import re
from requests import get
from tabulate import tabulate
import math

dir_dict = {
    270: "left",
    180: "top",
    90: "left",
    0: "top",
}

ppmm_dict = {
    "203": 8,
    "300": 11.81,
}

resp = get("https://print.niimbot.com/api/hardware/list")
resp.raise_for_status()
model_list = resp.json()["data"]["list"]
for m in model_list:
    m["name"] = re.sub(r"[\s\-]", "_", m["name"]).upper()


for dir_name, _, files in os.walk("docs"):
    for file_name in files:
        if not file_name.endswith(".md"):
            continue

        file_path = os.path.join(dir_name, file_name)

        with open(file_path, encoding="utf-8") as f:
            file_contents = f.read()

        if "<!-- BEGIN" not in file_contents:
            continue

        def replace_info(match):
            start, printer_name, end = match.groups()
            print("Filling ", printer_name, "block in", file_name)

            table = "ERROR"

            info = next(m for m in model_list if m["name"] == printer_name)
            if info is not None:
                head_px = math.ceil(
                    info["widthSetEnd"] * ppmm_dict[info["paccuracyName"]]
                )

                header = ["Parameter", "Value"]
                data = [
                    ["ID", ", ".join([str(i) for i in info["codes"]])],
                    ["Supported paper types", info["paperType"]],
                    ["DPI", info["paccuracyName"]],
                    [
                        "Printhead size",
                        f"{info['widthSetEnd']}mm ({head_px}px)",
                    ],
                    ["Print direction", dir_dict[info["printDirection"]]],
                ]
                table = tabulate(data, header, tablefmt="github")
            else:
                print("Model", printer_name, "not found")
            return f"{start}<!-- Auto-generated, do not edit -->\n{table}\n{end}"

        file_contents = re.sub(
            r"(<!-- BEGIN (\w+) CLOUD_INFO -->\n).*?(<!-- END CLOUD_INFO -->\n)",
            replace_info,
            file_contents,
            flags=re.DOTALL,
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_contents)
