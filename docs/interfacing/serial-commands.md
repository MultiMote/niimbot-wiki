# USB Serial debug commands

USB must me connected and printer must be turned off (charge mode).

## \#10001

Get hardware version and printer name (model+serial).

Example output:

```
#10001:V13.10,D110-G326030306,1
```

## \#10003

Get firmware version.

Example output:

```
#10003:13.14*21#
```

## test beep

Play sound.

## test motor [-] &lt;speed&gt; &lt;length&gt;

Turn motor.

## `test motor `

Stop motor.

## test get sensor

Some system sensors data.

## Other test commands (not all may be supported)

* test get id
* test set id `<id>` - set device name/serial
* test print
* test flash
* test rfid1
* test rfid2
* test unlock chip
* test get chip lock
* test rfidMode
* test exit
