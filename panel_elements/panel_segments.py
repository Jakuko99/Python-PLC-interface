from panel_interface.definitions.api_package import (
    TrackSegments,
    OutputPort,
    MemoryLocation,
)


class PanelSegments:
    segment_dict: dict[TrackSegments, dict[str, OutputPort]] = {
        TrackSegments.TU_ANDAC: {
            "occupied": OutputPort.TU_ANDAC_RED,
            "reserved": OutputPort.TU_ANDAC_YELLOW,
            "building": MemoryLocation.TU_ANDAC_BLINK,
        },
        TrackSegments.V1_FROG: {
            "occupied": OutputPort.V1_FROG_RED,
            "reserved": OutputPort.V1_FROG_YELLOW,
        },
        TrackSegments.V1_P: {
            "occupied": OutputPort.V1_P_RED,
            "reserved": OutputPort.V1_P_YELLOW,
        },
        TrackSegments.V1_M: {
            "occupied": OutputPort.V1_M_RED,
            "reserved": OutputPort.V1_M_YELLOW,
        },
        TrackSegments.V1_BRANCH_M: {
            "occupied": OutputPort.V1_BRANCH_M_RED,
            "reserved": OutputPort.V1_BRANCH_M_YELLOW,
        },
        TrackSegments.V2_FROG: {
            "occupied": OutputPort.V2_FROG_RED,
            "reserved": OutputPort.V2_FROG_YELLOW,
        },
        TrackSegments.V2_P: {
            "occupied": OutputPort.V2_P_RED,
            "reserved": OutputPort.V2_P_YELLOW,
        },
        TrackSegments.V2_M: {
            "occupied": OutputPort.V2_M_RED,
            "reserved": OutputPort.V2_M_YELLOW,
        },
        TrackSegments.V2_BRANCH_P: {
            "occupied": OutputPort.V2_BRANCH_P_RED,
            "reserved": OutputPort.V2_BRANCH_P_YELLOW,
        },
        TrackSegments.V3_P: {
            "occupied": OutputPort.V3_P_RED,
            "reserved": OutputPort.V3_P_YELLOW,
        },
        TrackSegments.V3_M: {
            "occupied": OutputPort.V3_M_RED,
            "reserved": OutputPort.V3_M_YELLOW,
        },
        TrackSegments.V3_BRANCH_P: {
            "occupied": OutputPort.V3_BRANCH_P_RED,
            "reserved": OutputPort.V3_BRANCH_P_YELLOW,
        },
        TrackSegments.V4_P: {
            "occupied": OutputPort.V4_P_RED,
            "reserved": OutputPort.V4_P_YELLOW,
        },
        TrackSegments.V4_M: {
            "occupied": OutputPort.V4_M_RED,
            "reserved": OutputPort.V4_M_YELLOW,
        },
        TrackSegments.V4_BRANCH_P: {
            "occupied": OutputPort.V4_BRANCH_P_RED,
            "reserved": OutputPort.V4_BRANCH_P_YELLOW,
        },
        TrackSegments.V5_FROG: {
            "occupied": OutputPort.V5_FROG_RED,
            "reserved": OutputPort.V5_FROG_YELLOW,
        },
        TrackSegments.V5_P: {
            "occupied": OutputPort.V5_P_RED,
            "reserved": OutputPort.V5_P_YELLOW,
        },
        TrackSegments.V5_M: {
            "occupied": OutputPort.V5_M_RED,
            "reserved": OutputPort.V5_M_YELLOW,
        },
        TrackSegments.V5_BRANCH_P: {
            "occupied": OutputPort.V5_BRANCH_P_RED,
            "reserved": OutputPort.V5_BRANCH_P_YELLOW,
        },
        TrackSegments.K1_MIDDLE: {"occupied": OutputPort.K1_MIDDLE_RED},
        TrackSegments.K2_MIDDLE: {"occupied": OutputPort.K2_MIDDLE_RED},
        TrackSegments.K3_MIDDLE: {"occupied": OutputPort.K3_MIDDLE_RED},
        TrackSegments.K4_MIDDLE: {"occupied": OutputPort.K4_MIDDLE_RED},
        TrackSegments.K1_EDGE: {
            "occupied": OutputPort.K1_EDGE_RED,
            "reserved": OutputPort.K1_YELLOW,
        },
        TrackSegments.K2_EDGE: {
            "occupied": OutputPort.K2_EDGE_RED,
            "reserved": OutputPort.K2_YELLOW,
        },
        TrackSegments.K3_EDGE: {
            "occupied": OutputPort.K3_EDGE_RED,
            "reserved": OutputPort.K3_YELLOW,
        },
        TrackSegments.K4_EDGE: {
            "occupied": OutputPort.K4_EDGE_RED,
            "reserved": OutputPort.K4_YELLOW,
        },
        TrackSegments.V6_FROG: {
            "occupied": OutputPort.V6_FROG_RED,
            "reserved": OutputPort.V6_FROG_YELLOW,
        },
        TrackSegments.V6_P: {
            "occupied": OutputPort.V6_P_RED,
            "reserved": OutputPort.V6_P_YELLOW,
        },
        TrackSegments.V6_M: {
            "occupied": OutputPort.V6_M_RED,
            "reserved": OutputPort.V6_M_YELLOW,
        },
        TrackSegments.V6_BRANCH_P: {
            "occupied": OutputPort.V6_BRANCH_P_RED,
            "reserved": OutputPort.V6_BRANCH_P_YELLOW,
        },
        TrackSegments.V6_BRANCH_M: {
            "occupied": OutputPort.V6_BRANCH_M_RED,
            "reserved": OutputPort.V6_BRANCH_M_YELLOW,
        },
        TrackSegments.V7_FROG: {
            "occupied": OutputPort.V7_FROG_RED,
            "reserved": OutputPort.V7_FROG_YELLOW,
        },
        TrackSegments.V7_P: {
            "occupied": OutputPort.V7_P_RED,
            "reserved": OutputPort.V7_P_YELLOW,
        },
        TrackSegments.V7_M: {
            "occupied": OutputPort.V7_M_RED,
            "reserved": OutputPort.V7_M_YELLOW,
        },
        TrackSegments.V7_BRANCH_P: {
            "occupied": OutputPort.V7_BRANCH_P_RED,
            "reserved": OutputPort.V7_BRANCH_P_YELLOW,
        },
        TrackSegments.V7_BRANCH_M: {
            "occupied": OutputPort.V7_BRANCH_M_RED,
            "reserved": OutputPort.V7_BRANCH_M_YELLOW,
        },
        TrackSegments.V8_FROG: {
            "occupied": OutputPort.V8_FROG_RED,
            "reserved": OutputPort.V8_FROG_YELLOW,
        },
        TrackSegments.V8_P: {
            "occupied": OutputPort.V8_P_RED,
            "reserved": OutputPort.V8_P_YELLOW,
        },
        TrackSegments.V8_M: {
            "occupied": OutputPort.V8_M_RED,
            "reserved": OutputPort.V8_M_YELLOW,
        },
        TrackSegments.V8_BRANCH_P: {
            "occupied": OutputPort.V8_BRANCH_P_RED,
            "reserved": OutputPort.V8_BRANCH_P_YELLOW,
        },
        TrackSegments.V9_FROG: {
            "occupied": OutputPort.V9_FROG_RED,
            "reserved": OutputPort.V9_FROG_YELLOW,
        },
        TrackSegments.V9_P: {
            "occupied": OutputPort.V9_P_RED,
            "reserved": OutputPort.V9_P_YELLOW,
        },
        TrackSegments.V9_M: {
            "occupied": OutputPort.V9_M_RED,
            "reserved": OutputPort.V9_M_YELLOW,
        },
        TrackSegments.V9_BRANCH_P: {
            "occupied": OutputPort.V9_BRANCH_P_RED,
            "reserved": OutputPort.V9_BRANCH_P_YELLOW,
        },
        TrackSegments.V10_FROG: {
            "occupied": OutputPort.V10_FROG_RED,
            "reserved": OutputPort.V10_FROG_YELLOW,
        },
        TrackSegments.V10_P: {
            "occupied": OutputPort.V10_P_RED,
            "reserved": OutputPort.V10_P_YELLOW,
        },
        TrackSegments.V10_M: {
            "occupied": OutputPort.V10_M_RED,
            "reserved": OutputPort.V10_M_YELLOW,
        },
        TrackSegments.V10_BRANCH_P: {
            "occupied": OutputPort.V10_BRANCH_P_RED,
            "reserved": OutputPort.V10_BRANCH_P_YELLOW,
        },
        TrackSegments.V11_FROG: {
            "occupied": OutputPort.V11_FROG_RED,
            "reserved": OutputPort.V11_FROG_YELLOW,
        },
        TrackSegments.V11_P: {
            "occupied": OutputPort.V11_P_RED,
            "reserved": OutputPort.V11_P_YELLOW,
        },
        TrackSegments.V11_M: {
            "occupied": OutputPort.V11_M_RED,
            "reserved": OutputPort.V11_M_YELLOW,
        },
        TrackSegments.V11_BRANCH_P: {
            "occupied": OutputPort.V11_BRANCH_P_RED,
            "reserved": OutputPort.V11_BRANCH_P_YELLOW,
        },
        TrackSegments.V12_FROG: {
            "occupied": OutputPort.V12_FROG_RED,
            "reserved": OutputPort.V12_FROG_YELLOW,
        },
        TrackSegments.V12_P: {
            "occupied": OutputPort.V12_P_RED,
            "reserved": OutputPort.V12_P_YELLOW,
        },
        TrackSegments.V12_M: {
            "occupied": OutputPort.V12_M_RED,
            "reserved": OutputPort.V12_M_YELLOW,
        },
        TrackSegments.V12_BRANCH_P: {
            "occupied": OutputPort.V12_BRANCH_P_RED,
            "reserved": OutputPort.V12_BRANCH_P_YELLOW,
        },
        TrackSegments._1_TU_1_CIFER: {
            "occupied": OutputPort._1_TU_1_CIFER_RED,
            "reserved": OutputPort._1_TU_1_CIFER_YELLOW,
        },
        TrackSegments._1_TU_2_CIFER: {
            "occupied": OutputPort._1_TU_2_CIFER_RED,
            "reserved": OutputPort._1_TU_2_CIFER_YELLOW,
        },
        TrackSegments._2_TU_1_CIFER: {
            "occupied": OutputPort._2_TU_1_CIFER_RED,
            "reserved": OutputPort._2_TU_1_CIFER_YELLOW,
        },
        TrackSegments._2_TU_2_CIFER: {
            "occupied": OutputPort._2_TU_2_CIFER_RED,
            "reserved": OutputPort._2_TU_2_CIFER_YELLOW,
        },
        TrackSegments._1B: {
            "occupied": OutputPort._1B_RED,
            "reserved": OutputPort._1B_YELLOW,
        },
        TrackSegments._2B: {
            "occupied": OutputPort._2B_RED,
            "reserved": OutputPort._2B_YELLOW,
        },
    }

    def segment_exists(self, segment: TrackSegments) -> bool:
        """
        Check if the segment exists in the segment dictionary.

        :param segment: The segment to check.
        :return: True if the segment exists, False otherwise.
        """
        return segment in self.segment_dict

    def get_segment(self, segment: TrackSegments) -> dict[str, OutputPort]:
        """
        Get the list of output ports associated with the segment.

        :param segment: The segment to get.
        :return: A list of output ports associated with the segment.
        """
        return self.segment_dict.get(segment, {})


panel_segments = PanelSegments()
