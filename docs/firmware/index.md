# Firmware file

## Official firmware files

Official firmware files is not publicly available.

The NIIMBOT app sends the printer model and version to the API server. If an update is available, the server can provide a URL for downloading the firmware.

This way the bunch of official firmware files was collected here: https://fw.niim.blue/

## Structure of update file

Applies to new firmware files starting with `0x18` byte. Byte order is little endian.

| Offset | Length | Example     | Description                                                      |
|--------|--------|-------------|------------------------------------------------------------------|
| 0x00   | 1      | 18          | Signature                                                        |
| 0x01   | 3      | 99 BE 4A    | Some random data, threat as zero when calculating header CRC     |
| 0x04   | 4      | 74 DF 01 00 | Length of firmware data                                          |
| 0x08   | 4      | 46 7A AC 3E | CRC32 of firmware data                                           |
| 0x0C   | 4      | 00 00 00 00 | Unknown                                                          |
| 0x10   | 4      | 00 00 00 00 | Unknown                                                          |
| 0x14   | 2      | 35 01       | Firmware Version                                                 |
| 0x16   | 2      | 10 03       | Unknown                                                          |
| 0x18   | 4      | FC E8 23 77 | CRC32 of previous data where bytes at 0x01-0x03 threated as zero |
| 0x1C   | ?      | 00 51 03 .. | Firmware data                                                    |

[ImHex pattern](files/niimbot_fw.hexpat)

[Firmware header editor](header-editor.html) (works in browser)
