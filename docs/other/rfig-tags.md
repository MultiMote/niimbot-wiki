# Label RFID tags

## Tricking the printer to not increment the counter

This may not work on all models/firmware versions. This will not work with the official app, as the counter there is synchronized with the cloud.

This method allows you to print on any thermal paper without using up the print counter.

- First, carefully remove the RFID tag from the roll if it is inside it.
- Open the printer lid.
- Place the RFID tag on the **outer** surface of the printer case, in the area closest to the antenna (usually the bottom).
- Close the printer lid. The printer should calibrate the paper gap as usual.
- Put the RFID tag away.

Do not bring the RFID tag close to the case again until it is turned off or the cover is opened, otherwise all missed prints will be recorded in the tag.

## RFID tag structure

RFID tags used in the printer are NTAG213 protected with 4-byte key. Label data is encrypted with TEA-ECB.

|     Page |      Offset |    Size | Field                    | Description                                                                 |
| -------: | ----------: | ------: | ------------------------ | --------------------------------------------------------------------------- |
|        0 |      `0x00` |       4 | UID[0:3] + BCC0          | UID bytes 0–2, followed by `BCC0`                                           |
|        1 |      `0x04` |       4 | UID[3:7]                 | Remaining 4 UID bytes                                                       |
|        2 |      `0x08` |       4 | BCC1 / internal / config | Width encoding is derived from byte 0; byte 1 is manufacturer/internal data |
|        3 |      `0x0C` |       4 | CC                       | Initialized as `E1 10 12 00`                                                |
|        4 |      `0x10` |       4 | OTP                      | Initialized as `01 03 A0 0C`                                                |
| **5–34** | `0x14–0x87` | **120** | **Encrypted label data** | TEA-ECB, 8-byte blocks                                                      |
|    35–39 | `0x8C–0x9F` |      20 | Unspecified/reserved     | No application fields defined by this source                                |
|       40 |      `0xA0` |       4 | Lock bytes               | `00 00 00 BD` default                                                       |
|       41 |      `0xA4` |       4 | Auth/config              | `00 00 00 04` default                                                       |
|       42 |      `0xA8` |       4 | CFG1                     | `C0 00 00 00` default                                                       |
|       43 |      `0xAC` |       4 | NTAG213 password         | Configurable 4-byte password                                                |
|       44 |      `0xB0` |       4 | PACK                     | Default `55 55 00 00`                                                       |

### Encrypted region schema

Compiled from various sources and checked with actual dumps. This is not 100% accurate.

| Offset | Size | Type        | Field                    | Notes                           |
| -----: | ---: | ----------- | ------------------------ | ------------------------------- |
| `0x00` |    2 | `uint16 LE` | Reserved                 |                                 |
| `0x02` |    2 | `uint16 LE` | Used paper / print count |                                 |
| `0x04` |    4 | `uint32 LE` | CRC32                    | CRC32 of `0x00..0x03`           |
| `0x08` |    7 | `bytes`     | UUID                     | `0x88 + UID[0..5]`              |
| `0x0F` |    1 | `uint8`     |                          |                                 |
| `0x10` |   16 | ASCII       | Serial                   | 0-terminated                    |
| `0x20` |    8 | `bytes`     |                          |                                 |
| `0x28` |   13 | ASCII       | Barcode                  | 0-terminated                    |
| `0x35` |    3 | `bytes`     |                          |                                 |
| `0x38` |    8 | `bytes`     |                          |                                 |
| `0x40` |    2 | `bytes`     |                          |                                 |
| `0x42` |    2 | `uint16 LE` | Roll metric (limit)      | Possibly [Print limit] * 6 // 5 |
| `0x44` |    1 | `uint8`     | Paper type               |                                 |
| `0x45` |    1 | `uint8`     | Density                  |                                 |
| `0x46` |   20 | ASCII       | Paper name               | 0-terminated                    |
| `0x5A` |    1 | `uint8`     | Width (mm)               | e.g. `0x28` = 40 mm             |
| `0x5B` |    1 | `uint8`     | Height (mm)              | e.g. `0x3C` = 60 mm             |
| `0x5C` |    1 | `uint8`     | Print limit              |                                 |
| `0x5D` |    2 | `bytes`     |                          |                                 |
| `0x5F` |    1 | `uint8`     | Gap (mm)                 |                                 |
| `0x60` |   20 | `bytes`     |                          |                                 |
| `0x74` |    4 | `uint32 LE` | CRC32                    | CRC32 of `0x08..0x73`           |

