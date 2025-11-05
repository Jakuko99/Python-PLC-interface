from S7_interface.s71200 import S71200
import logging

from S7_interface.definitions.api_package import (
    InputPort,
    OutputPort,
    MemoryLocation,
    SignalSign,
    Signals,
    TrackSegmentState,
    TrackSegments,
)
from S7_interface.panel_elements.api_package import panel_signals, panel_segments


class PanelInterface(S71200):
    def __init__(self, ip: str, debug: bool = False):
        super().__init__(ip, debug)
        self.ip: str = ip
        self.logger = logging.getLogger("App.PLC_interface")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("PLC interface initalized")

    def connect_plc(self) -> bool:
        result = self.connect()
        if result:
            self.logger.debug(f"Connected to PLC at {self.ip}")
        else:
            self.logger.error(f"Failed to connect to PLC at {self.ip}")
        return result

    def set_output(self, port: OutputPort, value: bool) -> bool:
        if port:
            self.writeMem(port.value, value)
            return True
        return False

    def get_input(self, port: InputPort) -> bool:
        if port:
            return self.getMem(port.value)
        return False

    def set_memory(self, address: MemoryLocation, value: bool) -> bool:
        if address:
            self.writeMem(address.value, value)
            return True
        return False

    def get_memory(self, address: MemoryLocation) -> bool:
        if address:
            return self.getMem(address.value)
        return False

    def set_signal(self, signal: Signals, sign: SignalSign) -> bool:
        """
        Set the signal value and sign.

        :param signal: The signal value to set.
        :param sign: The sign of the signal (e.g., SignalSign.STOP, SignalSign.FREE).
        """
        if panel_signals.signal_exists(signal):
            outputs: dict[str, OutputPort] = panel_signals.get_signal(signal)

            for output in outputs.values():
                self.set_output(output, False)  # reset all outputs first

            result: bool = False
            match sign:  # TODO: neeeds to logic for several types of signals
                case SignalSign.OFF:
                    pass
                case SignalSign.STOP:
                    result = self.set_output(outputs.get("red", None), True)
                case SignalSign.SUMMON:
                    result = self.set_output(outputs.get("white_blink", None), True)
                case SignalSign.FREE:
                    result = self.set_output(outputs.get("green", None), True)
                case SignalSign.SHUNT:
                    result = self.set_output(outputs.get("white", None), True)
                case SignalSign.WARN:
                    result = self.set_output(outputs.get("yellow", None), True)
                case _:
                    self.logger.error(f"Unknown signal sign: {sign}")
                    return False

            return result

        return False

    def set_track_segment(
        self, segment: TrackSegments, state: TrackSegmentState
    ) -> bool:
        """
        Set the track segment state.

        :param segment: The track segment to set.
        :param state: The state to set the track segment to (e.g., TrackSegmentState.FREE, TrackSegmentState.RESERVED).
        """
        if panel_segments.segment_exists(segment):
            outputs: dict[str, OutputPort] = panel_segments.get_segment(segment)

            for output in outputs.values():
                self.set_output(output, False)  # reset all outputs first

            result: bool = False
            match state:
                case TrackSegmentState.OCCUPIED:
                    result = self.set_output(outputs.get("occupied", None), True)
                case TrackSegmentState.RESERVED:
                    result = self.set_output(outputs.get("reserved", None), True)
                case TrackSegmentState.FREE:
                    pass  # all outputs are already reset
                case _:
                    self.logger.error(f"Unknown track segment state: {state}")
                    return False

            return result

        return False
