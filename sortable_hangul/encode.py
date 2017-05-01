from unicodedata import normalize

from typing import Generator, Tuple

from .constants import (
    BANGJEOM, C_JA, C_JA_2_JAMO, C_SY, C_SY_2_JA, C_SY_2_MO, C_SY_EXTEND,
    C_SY_EXTEND_2_JA, C_SY_EXTEND_2_MO, CP_JA, CP_JA_2_JAMO, HALF, HALF_2_JAMO,
    INDEX1100, INDEXA960, INDEXD7B0, INDEXD7CB, JAMO_EXTEND_A,
    JAMO_EXTEND_B_FINAL, JAMO_EXTEND_B_PEAK, JAMO_FINAL, JAMO_INITIAL,
    JAMO_PEAK, P_JA, P_JA_2_JAMO, P_SY, P_SY_2_JA, P_SY_2_MO)
from .types import CodeClass, CodeType


def encode_block_0(initial: int, peak: int) -> str:
    code_point = 0xF << (1 + 8)
    code_point += initial
    code_point = code_point << 7
    code_point += peak

    return chr(code_point)


def encode_block_1(final: int, bangjeom: int, type_: int) -> str:
    code_point = 0xF << 1
    code_point += 1
    code_point = code_point << 8

    if final:
        code_point += final

    code_point = code_point << (2 + 2)

    code_point += bangjeom

    code_point = code_point << 3

    code_point += type_

    return chr(code_point)


def unicode_decode(unicode_chr: str
                   ) -> Generator[Tuple[CodeClass, int, CodeType], None, None]:

    unicode_point = ord(unicode_chr)
    code_type = CodeType.NORMAL
    """
    Normalize Special Character
    """
    if JAMO_INITIAL[0] <= unicode_point < JAMO_FINAL[1]:
        # for performance
        code_points = [unicode_point]
    elif C_JA[0] <= unicode_point < C_JA[1]:
        code_points = [C_JA_2_JAMO[unicode_point - C_JA[0]]]
    elif C_SY[0] <= unicode_point < C_SY[1]:
        code_points = [
            C_SY_2_JA[unicode_point - C_SY[0]],
            C_SY_2_MO[unicode_point - C_SY[0]]
        ]
    elif C_SY_EXTEND[0] <= unicode_point < C_SY_EXTEND[1]:
        code_points = [
            C_SY_EXTEND_2_JA[unicode_point - C_SY_EXTEND[0]],
            C_SY_EXTEND_2_MO[unicode_point - C_SY_EXTEND[0]]
        ]
    elif CP_JA[0] <= unicode_point < CP_JA[1]:
        code_points = [CP_JA_2_JAMO[unicode_point - CP_JA[0]]]
    elif HALF[0] <= unicode_point < HALF[1]:
        code_points = [HALF_2_JAMO[unicode_point - HALF[0]]]
    elif P_JA[0] <= unicode_point < P_JA[1]:
        code_points = [P_JA_2_JAMO[unicode_point - P_JA[0]]]
    elif P_SY[0] <= unicode_point < P_SY[1]:
        code_points = [
            P_SY_2_JA[unicode_point - P_SY[0]],
            P_SY_2_MO[unicode_point - P_SY[0]]
        ]
    else:
        code_points = [unicode_point]

    for code_point in code_points:
        if JAMO_INITIAL[0] <= code_point < JAMO_INITIAL[1]:
            yield (CodeClass.INITIAL, INDEX1100[code_point - JAMO_INITIAL[0]],
                   code_type)
        elif JAMO_PEAK[0] <= code_point < JAMO_PEAK[1]:
            yield (CodeClass.PEAK, INDEX1100[code_point - JAMO_INITIAL[0]],
                   code_type)
        elif JAMO_FINAL[0] <= code_point < JAMO_FINAL[1]:
            yield (CodeClass.FINAL, INDEX1100[code_point - JAMO_INITIAL[0]],
                   code_type)
        elif JAMO_EXTEND_A[0] <= code_point < JAMO_EXTEND_A[1]:
            yield (CodeClass.INITIAL, INDEXA960[code_point - JAMO_EXTEND_A[0]],
                   code_type)
        elif JAMO_EXTEND_B_PEAK[0] <= code_point < JAMO_EXTEND_B_PEAK[1]:
            yield (CodeClass.PEAK,
                   INDEXD7B0[code_point - JAMO_EXTEND_B_PEAK[0]], code_type)
        elif JAMO_EXTEND_B_FINAL[0] <= code_point < JAMO_EXTEND_B_FINAL[1]:
            yield (CodeClass.PEAK,
                   INDEXD7CB[code_point - JAMO_EXTEND_B_FINAL[0]], code_type)
        elif BANGJEOM[0] <= code_point < BANGJEOM[1]:
            yield (CodeClass.BANGJEOM, code_point - BANGJEOM[0] + 1, code_type)
        else:
            yield None


def encode(unicode_text: str) -> str:
    unicode_text = normalize("NFD", unicode_text)

    for unicode_chr in unicode_text:
        for code_class, code_point, code_type in unicode_decode(unicode_chr):
            print(code_class, code_point, code_type)
