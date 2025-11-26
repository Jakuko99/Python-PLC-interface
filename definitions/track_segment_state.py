from enum import Enum, auto


class TrackSegmentState(Enum):
    FREE = 0
    OCCUPIED = 1
    RESERVED = 2
    PREPARING = 3