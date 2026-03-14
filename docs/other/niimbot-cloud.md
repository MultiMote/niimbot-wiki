# NIIMBOT cloud api

## getCloudTemplateByOneCode

Get label roll properties by unique id.

```http
POST https://print.niimbot.com/api/template/getCloudTemplateByOneCode HTTP/1.1
Content-Type: application/json
niimbot-user-agent: AppVersionName/999.0.0

{ "oneCode" : "02282280" }
```

## getRfid

Get label remaining prints and other info by serial number. Response is encrypted.

```http
POST https://print.niimbot.com/api/rfid/getRfid HTTP/1.1
Content-Type: application/json
niimbot-user-agent: OS/Android AppVersionName/999.0.0 DeviceId/xxx referer/CP001Mobile count/1111111

{ "serialNumber" : "PZ1G311330000385" }
```

## machineCascadeDetail

Check firmware update and some printer characteristics.

```http
POST https://print.niimbot.com/api/firmware/machineCascadeDetail HTTP/1.1
Content-Type: application/json
niimbot-user-agent: AppVersionName/999.0.0

{ "machineName" : "B1", "firmVersion": "5.10" }
```

Same for testing channel:

```http
POST https://print.jc-test.cn/api/firmware/machineCascadeDetail HTTP/1.1
Content-Type: application/json
niimbot-user-agent: AppVersionName/999.0.0

{ "machineName" : "B1", "firmVersion": "5.20" }
```

## devices.json

Get all NIIMBOT printers characteristics.

```http
GET https://print.niimbot.com/api/hardware/list HTTP/1.1
```

or

```http
GET https://oss-print.niimbot.com/public_resources/static_resources/devices.json HTTP/1.1
```

# industryTemplate/sizes

Gat all available template sizes

```http
GET https://print.niimbot.com/api/industryTemplate/sizes HTTP/1.1
niimbot-user-agent: AppVersionName/999.0.0
```

# industryTemplate/categories

Get template categories

```http
POST https://print.niimbot.com/api/industryTemplate/categories HTTP/1.1
Content-Type: application/json
niimbot-user-agent: AppVersionName/999.0.0

{
  "languageCode": "en",
  "width": 50,
  "height": 30,
  "limit": 10,
  "page": 1
}
```

# industryTemplate/page

Get templates by size

```http
POST https://print.niimbot.com/api/industryTemplate/page HTTP/1.1
Content-Type: application/json
niimbot-user-agent: AppVersionName/999.0.0

{
  "languageCode": "en",
  "width": 50,
  "height": 30,
  "limit": 256,
  "page": 1
}
```



# Other

```http
POST https://print.niimbot.com/api/industry/listIndustryCategoryMachineAdaptInfo HTTP/1.1
Content-Type: application/json
niimbot-user-agent: AppVersionName/999.0.0
```

