from enum import Enum, auto


class MemoryLocation(Enum):
    ALIVE = "MX0.5"
    RESET_VC = "MX1.4"

    L_WHITE_BLINK = "MX0.0"
    S1_WHITE_BLINK = "MX0.1"
    S2_WHITE_BLINK = "MX0.2"
    S3_WHITE_BLINK = "MX0.3"
    S4_WHITE_BLINK = "MX0.4"

    L1_WHITE_BLINK = "MX0.5"
    L2_WHITE_BLINK = "MX0.6"
    L3_WHITE_BLINK = "MX0.7"
    L4_WHITE_BLINK = "MX1.0"

    _1S_WHITE_BLINK = "MX1.1"
    _2S_WHITE_BLINK = "MX1.2"

    TU_ANDAC_BLINK = "MX1.3"
