from enum import Enum, auto


class SignalSign(Enum):
    OFF = auto()
    STOP = auto()
    SUMMON = auto()
    FREE = auto()
    SHUNT = auto()
    EXP40 = auto()
