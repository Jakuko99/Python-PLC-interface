from enum import Enum, auto


class MemoryLocation(Enum):
    L_WHITE_BLINK = "M%0.0"
    S1_WHITE_BLINK = "M%0.1"
    S2_WHITE_BLINK = "M%0.2"
    S3_WHITE_BLINK = "M%0.3"
    S4_WHITE_BLINK = "M%0.4"

    L1_WHITE_BLINK = "M%0.5"
    L2_WHITE_BLINK = "M%0.6"
    L3_WHITE_BLINK = "M%0.7"
    L4_WHITE_BLINK = "M%1.0"

    _1S_WHITE_BLINK = "M%1.1"
    _2S_WHITE_BLINK = "M%1.2"
