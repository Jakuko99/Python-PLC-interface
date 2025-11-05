from definitions.api_package import TrackSegments, OutputPort


class PanelSegments:
    segment_dict: dict[TrackSegments, dict[str, OutputPort]] = {
        TrackSegments.K1: {
            "occupied": OutputPort.K1_0,
            "reserved": OutputPort.K1_1,
        },
        TrackSegments.K2: {},  # and so on for other segments
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
