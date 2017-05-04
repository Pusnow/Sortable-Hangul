def pprint(ch: str) -> None:

    code_block = (ord(ch) >> 15) & 1

    if code_block:
        FINAL = (ord(ch) >> 7) & 0b11111111
        BANGJEOM = (ord(ch) >> 3) & 0b11
        TYPE = ord(ch) & 0b111
        print("FINAL-TYPE:", hex(FINAL), hex(BANGJEOM), hex(TYPE))

    else:
        INITIAL = (ord(ch) >> 7) & 0b11111111
        PEAK = ord(ch) & 0b1111111
        print("INITIAL-PEAK:", hex(INITIAL), hex(PEAK))
