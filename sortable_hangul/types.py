# -*- coding: utf-8 -*-
from enum import Enum
from typing import TypeVar, Tuple


class CodeClass(Enum):
    INITIAL = 1
    PEAK = 2
    FINAL = 3
    BANGJUM = 4


class CodeType(Enum):
    NORMAL = 1
    CP = 2
    H = 3
    C = 4
    P = 5


CodeBlock = TypeVar('CodeBlock', Tuple[CodeClass, int, CodeType], int)