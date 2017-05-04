from unicodedata import normalize

from typing import Generator

from .types import CodeBlock, CodeClass, CodeType

from .constants import (
    BANGJEOM, C_JA, C_JA_2_JAMO, C_SY, C_SY_2_JA, C_SY_2_MO, C_SY_EXTEND,
    C_SY_EXTEND_2_JA, C_SY_EXTEND_2_MO, CP_JA, CP_JA_2_JAMO, HALF, HALF_2_JAMO,
    INDEX1100, INDEXA960, INDEXD7B0, INDEXD7CB, JAMO_EXTEND_A,
    JAMO_EXTEND_B_FINAL, JAMO_EXTEND_B_PEAK, JAMO_FINAL, JAMO_INITIAL,
    JAMO_PEAK, P_JA, P_JA_2_JAMO, P_SY, P_SY_2_JA, P_SY_2_MO)


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


def unicode_decode(unicode_chr: str) -> Generator[CodeBlock, None, None]:

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
            yield code_point


def unicode_text_decode(unicode_text: str) -> Generator[CodeBlock, None, None]:
    for unicode_chr in unicode_text:
        for result in unicode_decode(unicode_chr):
            yield result


def encode_prev(prev_class: CodeClass, prev_point: int,
                prev_type: CodeType) -> str:

    if not prev_class:
        return ""

    if prev_class is CodeClass.INITIAL:
        return encode_block_0(prev_point, 0) + encode_block_1(0, 0, prev_type)
    elif prev_class is CodeClass.PEAK:
        return encode_block_1(0, 0, prev_type)
    elif prev_class is CodeClass.FINAL:
        return encode_block_1(prev_point, 0, prev_type)
    elif prev_class is CodeClass.BANGJEOM:
        return ""
    else:
        return ""


def encode(unicode_text: str) -> str:
    unicode_text = normalize("NFD", unicode_text)
    prev_class = CodeClass.NONE
    prev_point = 0
    prev_type = CodeType.NORMAL
    encoded_text = ""
    for code_block in unicode_text_decode(unicode_text):

        if type(code_block) is int:
            encoded_text += encode_prev(prev_class, prev_point, prev_type)
            encoded_text += chr(code_block)
            prev_class = CodeClass.NONE
            prev_point = 0
            prev_type = CodeType.NORMAL
        else:
            code_class, code_point, code_type = code_block

            if code_class is CodeClass.INITIAL:
                encoded_text += encode_prev(prev_class, prev_point, prev_type)
            elif code_class is CodeClass.PEAK:
                if prev_class is CodeClass.INITIAL:
                    encoded_text += encode_block_0(prev_point, code_point)
                else:
                    encoded_text += encode_prev(prev_class, prev_point,
                                                prev_type)
                    encoded_text += encode_block_0(0, code_point)
            elif code_class is CodeClass.FINAL:
                if prev_class is CodeClass.PEAK:
                    pass
                elif prev_class is CodeClass.INITIAL:
                    encoded_text += encode_block_0(prev_point, 0)
                else:
                    encoded_text += encode_prev(prev_class, prev_point,
                                                prev_type)
            elif code_class is CodeClass.BANGJEOM:
                if prev_class is CodeClass.FINAL:
                    encoded_text += encode_block_1(prev_point, code_point,
                                                   prev_type)
                elif prev_class is CodeClass.PEAK:
                    encoded_text += encode_block_1(0, code_point, prev_type)
                elif prev_class is CodeClass.INITIAL:
                    encoded_text += encode_block_0(prev_point, 0)
                    encoded_text += encode_block_1(0, code_point, prev_type)
                else:
                    encoded_text += encode_prev(prev_class, prev_point,
                                                prev_type)

            prev_class = code_class
            prev_point = code_point
            prev_type = code_type
    if prev_class is not CodeClass.NONE:
        encoded_text += encode_prev(prev_class, prev_point, prev_type)
    return encoded_text
