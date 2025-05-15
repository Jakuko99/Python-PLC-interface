from enum import Enum, auto


class TrackSegmentState(Enum):
    FREE = auto()
    OCCUPIED = auto()
    RESERVED = auto()
