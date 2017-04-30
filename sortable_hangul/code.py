from unicodedata import normalize

from .constants import (BANGJEOM, C_JA, C_SY, C_SY_EXTEND, CP_JA, HALF,
                        JAMO_EXTEND_A, JAMO_EXTEND_B_FINAL, JAMO_EXTEND_B_PEAK,
                        JAMO_FINAL, JAMO_INITIAL, JAMO_PEAK, P_JA, P_SY)

from .constants import INDEX1100, INDEXA960, INDEXD7B0, INDEXD7CB


def encode_block_0(initial: str, peak: str) -> str:
    code_point = 0xF << (1 + 8)

    initial_code = ord(initial)

    if JAMO_INITIAL[0] <= initial_code < JAMO_INITIAL[1]:
        code_point += INDEX1100[initial_code - JAMO_INITIAL[0]]
    elif JAMO_EXTEND_A[0] <= initial_code < JAMO_EXTEND_A[1]:
        code_point += INDEXA960[initial_code - JAMO_EXTEND_A[0]]
    else:
        raise

    code_point = code_point << 7

    peak_code = ord(peak)

    if JAMO_PEAK[0] <= peak_code < JAMO_PEAK[1]:
        code_point += INDEX1100[peak_code - JAMO_INITIAL[0]]
    elif JAMO_EXTEND_B_PEAK[0] <= peak_code < JAMO_EXTEND_B_PEAK[1]:
        code_point += INDEXD7B0[peak_code - JAMO_EXTEND_B_PEAK[0]]
    else:
        raise
    return chr(code_point)


def encode_block_1(final: str, bangjeom: int, type_: int) -> str:
    code_point = 0xF << 1
    code_point += 1
    code_point = code_point << 8

    if final:
        final_code = ord(final)

        if JAMO_FINAL[0] <= final_code < JAMO_FINAL[1]:
            code_point += INDEX1100[final_code - JAMO_INITIAL[0]]
        elif JAMO_EXTEND_B_FINAL[0] <= final_code < JAMO_EXTEND_B_FINAL[1]:
            code_point += INDEXD7CB[final_code - JAMO_EXTEND_B_FINAL[0]]
        else:
            raise

    code_point = code_point << (2 + 2)

    code_point += bangjeom

    code_point = code_point << 3

    code_point += type_

    return chr(code_point)


def normalize_jamo(unicode_chr: str) -> (int, str):

    code_point = ord(unicode_chr)

    if JAMO[0] <= code_point < JAMO[1]:
        return (0, unicode_chr)


def encode(unicode_text: str) -> str:
    unicode_text = normalize("NFD", unicode_text)
