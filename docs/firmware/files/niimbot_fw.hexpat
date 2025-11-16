import std.io;
import std.hash;

struct FirmwareHeader {
    u8 signature;
    u8 random_data[3];
    u32 fw_length;
    u32 fw_crc;
    u32 unknown1;
    u32 unknown2;
    u8 fw_version[2];
    u8 unknown3[2];
    u32 header_crc;
};

struct NiimbotUpdate {
    FirmwareHeader header;
    u8 fw_data[header.fw_length];
};

NiimbotUpdate update @ 0x0;

u8 crc_buf[24];
for (u32 i = 0, i < 24, i=i+1) { crc_buf[i] = (i == 1 || i== 2 || i== 3) ? 0 : $[i]; }

u32 header_crc = std::hash::crc32(crc_buf, 0xFFFFFFFF, 0x4c11db7, 0xFFFFFFFF, true, true);
std::print("HEADER CRC {0} (calc={1:X} found={2:X})", update.header.header_crc == header_crc ? "OK" : "ERR", update.header.header_crc, header_crc);

u32 fw_crc = std::hash::crc32(update.fw_data, 0xFFFFFFFF, 0x4c11db7, 0xFFFFFFFF, true, true);
std::print("FW CRC {0} (calc={1:X} found={2:X})", update.header.fw_crc == fw_crc ? "OK" : "ERR", update.header.fw_crc, fw_crc);
