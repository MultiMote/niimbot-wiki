# Firmware file

## Official firmware files

Official firmware files is not publicly available.

The NIIMBOT app sends the printer model and version to the API server. If an update is available, the server can provide a URL for downloading the firmware.

This way the bunch of official firmware files was collected here: https://fw.niim.blue/

## Structure of firmware file

Applies to new firmware files starting with `0x18` byte. Byte order is little endian.

| Offset | Length | Example       | Description                                                      |
|--------|--------|---------------|------------------------------------------------------------------|
| 0x00   | 1      | `18`          | Signature                                                        |
| 0x01   | 3      | `99 BE 4A`    | Some random data, threat as zero when calculating header CRC     |
| 0x04   | 4      | `74 DF 01 00` | Length of firmware data                                          |
| 0x08   | 4      | `46 7A AC 3E` | CRC32 of firmware data                                           |
| 0x0C   | 4      | `00 00 00 00` | Reserved                                                         |
| 0x10   | 4      | `00 00 00 00` | Reserved                                                         |
| 0x14   | 2      | `35 01`       | Firmware Version                                                 |
| 0x16   | 2      | `10 03`       | Device model ID                                                  |
| 0x18   | 4      | `FC E8 23 77` | CRC32 of previous data where bytes at 0x01-0x03 threated as zero |
| 0x1C   | ?      | `00 51 03 ..` | Firmware data                                                    |

[ImHex pattern](files/niimbot_fw.hexpat)

[Firmware header editor](header-editor.html) (works in browser)

## Structure of compressed firmware file

First seen in B1 PRO. Compressed with DEFLATE algorithm.

| Offset | Length | Example       | Description                                                         |
| ------ | ------ | ------------- | ------------------------------------------------------------------- |
| `0x00` | 1      | `18`          | Signature                                                           |
| `0x01` | 3      | `99 BE 4A`    | Some random data, treated as zero when calculating header CRC       |
| `0x04` | 4      | `XX XX XX XX` | Length of compressed payload                                        |
| `0x08` | 4      | `XX XX XX XX` | CRC32 of compressed payload                                         |
| `0x0C` | 4      | `00 00 00 00` | Reserved                                                            |
| `0x10` | 4      | `00 00 00 00` | Reserved                                                            |
| `0x14` | 2      | `35 01`       | Firmware Version                                                    |
| `0x16` | 2      | `10 03`       | Device model ID                                                     |
| `0x18` | 4      | `XX XX XX XX` | CRC32 of header `0x00-0x17`, with bytes `0x01-0x03` treated as zero |
| `0x1C` | 4      | `XX XX XX XX` | Uncompressed firmware size                                          |
| `0x20` | 4      | `00 80 00 00` | Compression block size, normally `0x8000` (32768)                   |
| `0x24` | 4      | `XX XX XX XX` | Block 0 record length = `4 + compressed size`                       |
| `0x28` | 4      | `00 80 00 00` | Block 0 uncompressed size                                           |
| `0x2C` | ?      | `...`         | Block 0 raw DEFLATE data                                            |
| `...`  | 4      | `XX XX XX XX` | Next block record length = `4 + compressed size`                    |
| `...`  | 4      | `XX XX XX XX` | Next block uncompressed size                                        |
| `...`  | ?      | `...`         | Next block raw DEFLATE data                                         |
| `...`  | ...    | ...           | Repeated until entire firmware is represented                       |

[Firmware repacker](firmware-repacker.html) (works in browser)

Firmware structure and compression algorithm was reverse engineered by mode01.
