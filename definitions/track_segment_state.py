from enum import Enum, auto


class TrackSegmentState(Enum):
    FREE = 0
    OCCUPIED = 1
    OCCUPIED_FULL = 2
    RESERVED = 3
    PREPARING = 4
    FAILURE = 5