from enum import Enum, auto


class SignalSign(Enum):
    OFF = 0
    STOP = 1
    SUMMON = 2
    FREE = 3
    SHUNT = 4
    WARN = 5