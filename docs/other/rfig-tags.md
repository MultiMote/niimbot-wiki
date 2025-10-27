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

todo [^1]


```
cryoz
on Dec 14, 2024 · edited by cryoz

well, some results from firmware:
1)rfid encrypted with TEA, from block 5 to block 34
2) tea key: <removed>
when decrypted:
3) block5 - count of printed pages?
4) block 6 = CRC32(block5) (4 bytes)
5) block 34 = CRC32(block7..block33) (108 bytes)

tywtyw2002
on Dec 15, 2024 · edited by tywtyw2002

I did this long time ago, some detailed information already forgot...

block 5 is printed label cnt.
block 7-8 uuid
block 9-12 serial ASCII
block 15-16 barcode
block 21 first 2bytes is print limited cnt (2bytes short)
```

[^1]: [B21: Hack to not waste labels during testing](https://github.com/AndBondStyle/niimprint/issues/34)
