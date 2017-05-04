# -*- coding: utf-8 -*-
from enum import Enum, IntEnum
from typing import TypeVar, Tuple


class CodeClass(Enum):
    INITIAL = 0
    PEAK = 1
    FINAL = 2
    BANGJEOM = 3
    NONE = 4


class CodeType(IntEnum):
    NORMAL = 0
    H = 1
    CP = 2
    P = 3
    C = 4


CodeBlock = TypeVar('CodeBlock', Tuple[CodeClass, int, CodeType], int)
