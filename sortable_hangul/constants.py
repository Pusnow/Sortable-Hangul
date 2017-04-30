# -*- coding: utf-8 -*-

# Code Points

JAMO_INITIAL = (0x1100, 0x1160)
JAMO_PEAK = (0x1160, 0x11A8)
JAMO_FINAL = (0x11A8, 0x1200)
JAMO_EXTEND_A = (0xA960, 0xA97D)
JAMO_EXTEND_B_PEAK = (0xD780, 0xD7C7)
JAMO_EXTEND_B_FINAL = (0xD7D0, 0xD7FC)
BANGJEOM = (0x302E, 0x3030)

CP_JA = (0x3131, 0x318F)

P_JA = (0x3200, 0x320E)
P_SY = (0X320E, 0x321D)

C_JA = (0x3260, 0x326E)
C_SY = (0x326E, 0x327C)
C_SY_EXTEND = (0x327E, 0x327F)

HALF = (0xFFA0, 0xFFDD)

# Conversion Tables

CP_JA_2_JAMO = (0x1100, 0x1101, 0x11AA, 0x1102, 0x11AC, 0x11AD, 0x1103, 0x1104,
                0x1105, 0x11B0, 0x11B1, 0x11B2, 0x11B3, 0x11B4, 0x11B5, 0x111A,
                0x1106, 0x1107, 0x1108, 0x1121, 0x1109, 0x110A, 0x110B, 0x110C,
                0x110D, 0x110E, 0x110F, 0x1110, 0x1111, 0x1112, 0x1161, 0x1162,
                0x1163, 0x1164, 0x1165, 0x1166, 0x1167, 0x1168, 0x1169, 0x116A,
                0x116B, 0x116C, 0x116D, 0x116E, 0x116F, 0x1170, 0x1171, 0x1172,
                0x1173, 0x1174, 0x1175, 0x1160, 0x1114, 0x1115, 0x11C7, 0x11C8,
                0x11CC, 0x11CE, 0x11D3, 0x11D7, 0x11D9, 0x111C, 0x11DD, 0x11DF,
                0x111D, 0x111E, 0x1120, 0x1122, 0x1123, 0x1127, 0x1129, 0x112B,
                0x112C, 0x112D, 0x112E, 0x112F, 0x1132, 0x1136, 0x1140, 0x1147,
                0x114C, 0x11F1, 0x11F2, 0x1157, 0x1158, 0x1159, 0x1184, 0x1185,
                0x1188, 0x1191, 0x1192, 0x1194, 0x119E, 0x11A1, )

P_JA_2_JAMO = (0x1100, 0x1102, 0x1103, 0x1105, 0x1106, 0x1107, 0x1109, 0x110B,
               0x110C, 0x110E, 0x110F, 0x1110, 0x1111, 0x1112, )
P_SY_2_JA = (0x1100, 0x1102, 0x1103, 0x1105, 0x1106, 0x1107, 0x1109, 0x110B,
             0x110C, 0x110E, 0x110F, 0x1110, 0x1111, 0x1112, 0x110C, )
P_SY_2_MO = (0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161,
             0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x116E, )

C_JA_2_JAMO = (0x1100, 0x1102, 0x1103, 0x1105, 0x1106, 0x1107, 0x1109, 0x110B,
               0x110C, 0x110E, 0x110F, 0x1110, 0x1111, 0x1112, )
C_SY_2_JA = (0x1100, 0x1102, 0x1103, 0x1105, 0x1106, 0x1107, 0x1109, 0x110B,
             0x110C, 0x110E, 0x110F, 0x1110, 0x1111, 0x1112, )
C_SY_2_MO = (0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161,
             0x1161, 0x1161, 0x1161, 0x1161, 0x1161, 0x1161, )
C_SY_EXTEND_2_JA = (0x110B, )
C_SY_EXTEND_2_MO = (0x116E, )

HALF_2_JAMO = (0x1160, 0x1100, 0x1101, 0x11AA, 0x1102, 0x11AC, 0x11AD, 0x1103,
               0x1104, 0x1105, 0x11B0, 0x11B1, 0x11B2, 0x11B3, 0x11B4, 0x11B5,
               0x111A, 0x1106, 0x1107, 0x1108, 0x1121, 0x1109, 0x110A, 0x110B,
               0x110C, 0x110D, 0x110E, 0x110F, 0x1110, 0x1111, 0x1112, 0xFFBF,
               0xFFC0, 0xFFC1, 0x1161, 0x1162, 0x1163, 0x1164, 0x1165, 0x1166,
               0xFFC8, 0xFFC9, 0x1167, 0x1168, 0x1169, 0x116A, 0x116B, 0x116C,
               0xFFD0, 0xFFD1, 0x116D, 0x116E, 0x116F, 0x1170, 0x1171, 0x1172,
               0xFFD8, 0xFFD9, 0x1173, 0x1174, 0x1175, 0xFFDD, 0xFFDE,
               0xFFDF, )

# The order values for Johab Hangul Letters 0x1100 - 0x11FF
INDEX1100 = (
    0x01, 0x02, 0x0c, 0x18, 0x1a, 0x24, 0x46, 0x56, 0x5d, 0x6d, 0x76, 0x8a,
    0xa1, 0xa5, 0xab, 0xb0, 0xb1, 0xb3, 0xb9, 0x0d, 0x0e, 0x0f, 0x11, 0x19,
    0x29, 0x2d, 0x42, 0x45, 0x4d, 0x55, 0x57, 0x58, 0x59, 0x5e, 0x5f, 0x60,
    0x61, 0x62, 0x63, 0x65, 0x66, 0x68, 0x69, 0x6b, 0x6c, 0x6e, 0x6f, 0x70,
    0x71, 0x72, 0x73, 0x74, 0x7a, 0x7c, 0x7d, 0x7e, 0x7f, 0x80, 0x81, 0x82,
    0x83, 0x84, 0x85, 0x86, 0x87, 0x8b, 0x8c, 0x8e, 0x8f, 0x90, 0x91, 0x92,
    0x93, 0x94, 0x95, 0x96, 0x98, 0xa4, 0xa7, 0xa8, 0xa9, 0xaa, 0xac, 0xad,
    0xae, 0xaf, 0xb4, 0xb8, 0xbf, 0xc0, 0x04, 0x12, 0x14, 0x17, 0x1c, 0xc2,
    0x00, 0x01, 0x05, 0x06, 0x0a, 0x0b, 0x0f, 0x10, 0x14, 0x15, 0x16, 0x17,
    0x21, 0x22, 0x2b, 0x2e, 0x30, 0x34, 0x36, 0x40, 0x47, 0x49, 0x02, 0x03,
    0x07, 0x08, 0x0c, 0x0d, 0x0e, 0x12, 0x13, 0x1a, 0x1b, 0x1d, 0x1e, 0x20,
    0x25, 0x26, 0x28, 0x29, 0x2a, 0x2c, 0x2d, 0x2f, 0x32, 0x33, 0x37, 0x39,
    0x3a, 0x3b, 0x3c, 0x3e, 0x3f, 0x45, 0x46, 0x48, 0x4a, 0x4b, 0x50, 0x53,
    0x55, 0x57, 0x58, 0x5a, 0x5c, 0x5d, 0x5e, 0x04, 0x09, 0x11, 0x18, 0x19,
    0x01, 0x02, 0x07, 0x0c, 0x14, 0x17, 0x18, 0x24, 0x25, 0x2f, 0x33, 0x3a,
    0x40, 0x41, 0x42, 0x46, 0x56, 0x5e, 0x6d, 0x76, 0x8a, 0xa1, 0xab, 0xb0,
    0xb1, 0xb3, 0xb9, 0x05, 0x08, 0x0d, 0x0f, 0x12, 0x13, 0x16, 0x19, 0x1c,
    0x27, 0x29, 0x2a, 0x2c, 0x2d, 0x30, 0x31, 0x36, 0x38, 0x39, 0x3b, 0x3c,
    0x3f, 0x43, 0x47, 0x4b, 0x4d, 0x4f, 0x50, 0x51, 0x53, 0x54, 0x55, 0x5a,
    0x69, 0x6a, 0x6b, 0x6e, 0x70, 0x71, 0x73, 0x87, 0x99, 0x9a, 0x9e, 0x9f,
    0x98, 0x9c, 0x9d, 0xb4, 0xb8, 0xba, 0xbb, 0xbc, 0xbd, 0xc0, 0x03, 0x06,
    0x09, 0x0a, 0x0b, 0x0e, )

# The order values for Johab Hangul Syllable-Initial Letters 0xA960 - 0xA97C
INDEXA960 = (0x1d, 0x1e, 0x1f, 0x21, 0x25, 0x26, 0x2a, 0x2b, 0x2f, 0x33, 0x35,
             0x39, 0x3a, 0x3e, 0x3f, 0x47, 0x4a, 0x4f, 0x64, 0x67, 0x6a, 0x79,
             0x8d, 0x97, 0xa6, 0xb2, 0xb7, 0xbe, 0xc1, )

# The order values for Johab Hangul Syllable-Peak Letters 0xD7B0 - 0xD7C6
INDEXD7B0 = (0x1c, 0x1f, 0x23, 0x24, 0x27, 0x31, 0x35, 0x38, 0x3d, 0x41, 0x42,
             0x43, 0x44, 0x4c, 0x4d, 0x4e, 0x4f, 0x51, 0x52, 0x54, 0x56, 0x59,
             0x5b, )

# The order values for Johab Hangul Syllable-Final Letters 0xD7CB - 0xD7FB
INDEXD7CB = (0x10, 0x15, 0x1a, 0x1b, 0x1e, 0x1f, 0x20, 0x21, 0x22, 0x23, 0x26,
             0x28, 0x2e, 0x32, 0x34, 0x37, 0x3d, 0x44, 0x45, 0x48, 0x49, 0x4c,
             0x4e, 0x52, 0x59, 0x5b, 0x5c, 0x5d, 0x60, 0x65, 0x66, 0x72, 0x75,
             0x77, 0x78, 0x7b, 0x7d, 0x7e, 0x80, 0x82, 0x88, 0x89, 0x9b, 0xa0,
             0xa2, 0xa3, 0xa5, 0xb5, 0xb6, )