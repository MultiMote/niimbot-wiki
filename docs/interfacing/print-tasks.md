# Print tasks

Unfortunately, print sequence is not same across different printer models.
In order to support a wide model range, print tasks are used.

The name of the print task does not necessarily represent the only model it will work with.

## D11_V1

Used in old D11 models.

Print progress is fetched by continuously waiting `In_PrinterPageIndex` packet with `payload == total pages`.

```
Client                              Printer
  │                                    │
  │── SetDensity (0x21) ──────────────►│  payload: [density(u8)]
  │── SetLabelType (0x23) ────────────►│  payload: [type(u8)]
  │── PrintStart (0x01, 1b) ──────────►│  payload: [0x01]
  │                                    │
  │  ↻ per page loop:                  │
  │── PrintClear (0x20) ──────────────►│  payload: [0x01]
  │── PageStart (0x03) ───────────────►│  payload: [0x01]
  │── SetPageSize (0x13, 2b) ─────────►│  payload: [rows(u16)]
  │── PrintQuantity (0x15) ───────────►│  payload: [quantity(u16)]
  │── Write Image Data ───────────────►│  one-way: PrintEmptyRow (0x84) | PrintBitmapRow (0x85) | PrintBitmapRowIndexed (0x83)
  │── PageEnd (0xe3) ─────────────────►│  payload: [0x01]
  │                                    │
  │  ↻ status polling loop:            │
  │◄─ In_PrinterPageIndex (0xe0) ──────┤  wait until payload(u16) == total pages
  │                                    │
  │── PrintEnd (0xf3) ────────────────►│  payload: [0x01]
```

## B21_V1

Print progress is fetched by continuously sending `PrintEnd`. Print is finished when `payload == 1`.

```
Client                              Printer
  │                                    │
  │── SetDensity (0x21) ──────────────►│  payload: [density(u8)]
  │── SetLabelType (0x23) ────────────►│  payload: [type(u8)]
  │── PrintStart (0x01, 1b) ──────────►│  payload: [0x01]
  │                                    │
  │  ↻ per page loop:                  │
  │── PageStart (0x03) ───────────────►│  payload: [0x01]
  │── SetPageSize (0x13, 4b) ─────────►│  payload: [rows(u16), cols(u16)]
  │── Write Image Data ───────────────►│  one-way: PrintEmptyRow (0x84) | PrintBitmapRow (0x85) | PrintBitmapRowIndexed (0x83)
  │── PrinterCheckLine (0x86) ────────►│  payload: [line(u16), 0x01] (every 200 lines)
  │── PageEnd (0xe3) ─────────────────►│  payload: [0x01]
  │                                    │
  │  ↻ status polling loop:            │
  │── PrintEnd (0xf3) ────────────────►│  payload: [0x01]
  │◄─ In_PrintEnd (0xf4) ──────────────┤  payload: [0x00 - still printing, 0x01 - finished]
```

## B21_L2B

Print progress is tracked page-by-page via `pageEnd()` responses and emitted progress events.

```
Client                              Printer
  │                                    │
  │── SetDensity (0x21) ──────────────►│  payload: [density(u8)]
  │── SetLabelType (0x23) ────────────►│  payload: [type(u8)]
  │── PrintStart (0x01, 1b) ──────────►│  payload: [0x01]
  │                                    │
  │  ↻ per page loop:                  │
  │── PageStart (0x03) ───────────────►│  poll until true
  │── SetPageSize (0x13, 4b) ─────────►│  payload: [rows(u16), cols(u16)]
  │── Write Image Data ───────────────►│  one-way: PrintEmptyRow (0x84) | PrintBitmapRow (0x85) | PrintBitmapRowIndexed (0x83)
  │── PrinterCheckLine (0x86) ────────►│  payload: [line(u16), 0x01] (every 200 lines)
  │                                    │
  │  ↻ status polling loop             │
  │     (part of page loop):           │
  │── PageEnd (0xe3) ─────────────────►│  payload: [0x01]
  │◄─ In_PageEnd (0xe4) ───────────────┤  payload: [0x00 - still printing, 0x01 - finished]
  │                                    │
  │── PrintEnd (0xf3) ────────────────►│  payload: [0x01]
```

## D110

Used in 203 DPI D110, D11.

Print progress is fetched by continuously sending `PrintStatus`.

```
Client                              Printer
  │                                    │
  │── SetDensity (0x21) ──────────────►│  payload: [density(u8)]
  │── SetLabelType (0x23) ────────────►│  payload: [type(u8)]
  │── PrintStart (0x01, 1b) ──────────►│  payload: [0x01]
  │                                    │
  │  ↻ per page loop:                  │
  │── PrintClear (0x20) ──────────────►│  payload: [0x01]
  │── PageStart (0x03) ───────────────►│  payload: [0x01]
  │── SetPageSize (0x13, 4b) ─────────►│  payload: [rows(u16), cols(u16)]
  │── PrintQuantity (0x15) ───────────►│  payload: [quantity(u16)]
  │── Write Image Data ───────────────►│  one-way: PrintEmptyRow (0x84) | PrintBitmapRow (0x85) | PrintBitmapRowIndexed (0x83)
  │── PageEnd (0xe3) ─────────────────►│  payload: [0x01]
  │                                    │
  │  ↻ status polling loop:            │
  │── PrintStatus (0xa3) ─────────────►│  poll page status
  │◄─ In_PrintStatus (0xb3) ───────────┤  payload: [pageIndex(u16), ...], print is finished when pageIndex == totalPages
  │                                    │
  │── PrintEnd (0xf3) ────────────────►│  payload: [0x01]
```

## H1S

Print progress is fetched by continuously sending `PrintStatus`.

```
Client                              Printer
  │                                    │
  │── SetDensity (0x21) ──────────────►│  payload: [density(u8)]
  │── SetLabelType (0x23) ────────────►│  payload: [type(u8)]
  │── PrintStart (0x01, 2b) ──────────►│  payload: [totalPages(u16)]
  │                                    │
  │  ↻ per page loop:                  │
  │── PageStart (0x03) ───────────────►│  payload: [0x01]
  │── SetPageSize (0x13, 9b) ─────────►│  payload: [rows(u16), cols(u16), copiesCount(u16), cutHeight(u16), cutType(u8)]
  │── Write Image Data ───────────────►│  one-way: PrintEmptyRow (0x84) | PrintBitmapRow (0x85) | PrintBitmapRowIndexed (0x83)
  │── PageEnd (0xe3) ─────────────────►│  payload: [0x01]
  │                                    │
  │  ↻ status polling loop:            │
  │── PrintStatus (0xa3) ─────────────►│  poll page status
  │◄─ In_PrintStatus (0xb3) ───────────┤  payload: [pageIndex(u16), ...], print is finished when pageIndex == totalPages
  │                                    │
  │── PrintEnd (0xf3) ────────────────►│  payload: [0x01]
```

## B1

Used in most printers released in 2024.

Print progress is fetched by continuously sending `PrintStatus`.

```
Client                              Printer
  │                                    │
  │── SetDensity (0x21) ──────────────►│  payload: [density(u8)]
  │── SetLabelType (0x23) ────────────►│  payload: [type(u8)]
  │── PrintStart (0x01, 7b) ──────────►│  payload: [totalPages(u16), 0x00, 0x00, 0x00, 0x00, pageColor(u8)]
  │                                    │
  │  ↻ per page loop:                  │
  │── PageStart (0x03) ───────────────►│  payload: [0x01]
  │── SetPageSize (0x13, 6b) ─────────►│  payload: [rows(u16), cols(u16), copiesCount(u16)]
  │── Write Image Data ───────────────►│  one-way: PrintEmptyRow (0x84) | PrintBitmapRow (0x85) | PrintBitmapRowIndexed (0x83)
  │── PageEnd (0xe3) ─────────────────►│  payload: [0x01]
  │                                    │
  │  ↻ status polling loop:            │
  │── PrintStatus (0xa3) ─────────────►│  poll page status
  │◄─ In_PrintStatus (0xb3) ───────────┤  payload: [pageIndex(u16), ...], print is finished when pageIndex == totalPages
  │                                    │
  │── PrintEnd (0xf3) ────────────────►│  payload: [0x01]
```

`pageColor` default is `0` (SingleColor).


## D110M_V4

Used in most printers released in 2025. It's the most current at the moment.

Print progress is fetched by continuously sending `PrintStatus`. `PageStart` command is not used.

```
Client                              Printer
  │                                    │
  │── SetLabelType (0x23) ────────────►│  payload: [type(u8)]
  │── SetDensity (0x21) ──────────────►│  payload: [density(u8)]
  │── TubeTypeAndWidth (0x0f) ────────►│  payload: [0x01, 0x01, tubeType(u8), widthFixed(u16)] (optional)
  │── HalfCut (0x5c) ─────────────────►│  payload: [0x01, enable(u8)] (optional)
  │── PrintStart (0x01, 9b) ──────────►│  payload: [totalPages(u16), 0x00, 0x00, 0x00, 0x00, pageColor(u8), speed(u8), someFlag(u8)]
  │                                    │
  │  ↻ per page loop:                  │
  │── PrintStatus (0xa3) ─────────────►│  one-way (don't wait response)
  │── SetPageSize (0x13, 13b / 45b) ──►│  payload: [rows(u16), cols(u16), copiesCount(u16), cutHeight(u16), cutType(u8), 0x00, sendAll(u8), partHeight(u16), serial(32b)]
  │── Write Image Data ───────────────►│  PrintEmptyRow (0x84) | PrintBitmapRow (0x85) | PrintBitmapRowIndexed (0x83) | PrintBitmapRowDoubleColor (0x8a)
  │── PageEnd (0xe3) ─────────────────►│  payload: [0x01]
  │                                    │
  │  ↻ status polling loop:            │
  │── PrintStatus (0xa3) ─────────────►│  poll page status
  │◄─ In_PrintStatus (0xb3) ───────────┤
  │                                    │
  │── PrintEnd (0xf3) ────────────────►│  payload: [0x01]
  │── Heartbeat (0xdc) ───────────────►│  one-way (don't wait response)
```

`pageColor`: `0` (SingleColor), `1` (DoubleColor).

`speed`: `0` (quality), `1` (speed).

!!! note

    B21_PRO note

    For some reason this printer drops the first packet after `PrintStart` if using Bluetooth connection.
    Originally `PrintStatus` is sent and no response waited.

    Also printer drops the first packet after `PrintEnd`.
    Originally `Heartbeat` is sent and no response waited.
