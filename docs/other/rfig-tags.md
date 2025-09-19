# Label RFID tags

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
