from panel_interface.s71200 import S71200
import logging

from panel_interface.definitions.api_package import (
    InputPort,
    OutputPort,
    MemoryLocation,
    SignalSign,
    Signals,
    TrackSegmentState,
    TrackSegments,
    DatabaseLocation,
    ButtonDB,
)
from panel_interface.panel_elements.api_package import panel_signals, panel_segments


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

    def get_signal_sign(self, signal: Signals) -> SignalSign:
        """
        Get the signal sign.

        :param signal: The signal to get.
        : return: The sign of the signal (e.g., SignalSign.STOP, SignalSign.FREE).
        """

        if panel_signals.signal_exists(signal):
            outputs: dict[str, OutputPort] = panel_signals.get_signal(signal)

            if outputs.get("red", None) and self.get_output(outputs.get("red", None)):
                return SignalSign.STOP

            elif outputs.get("white_blink", None) and self.get_memory(
                outputs.get("white_blink", None)
            ):
                return SignalSign.SUMMON

            elif outputs.get("green", None) and self.get_output(
                outputs.get("green", None)
            ):
                return SignalSign.FREE

            elif outputs.get("white", None) and self.get_output(
                outputs.get("white", None)
            ):
                return SignalSign.SHUNT

            elif outputs.get("yellow", None) and self.get_output(
                outputs.get("yellow", None)
            ):
                return SignalSign.WARN

            else:
                return SignalSign.OFF

        return SignalSign.OFF

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
                case TrackSegmentState.BUILDING:
                    result = self.set_output(outputs.get("building", None), True)
                case TrackSegmentState.FREE:
                    pass  # all outputs are already reset
                case _:
                    self.logger.error(f"Unknown track segment state: {state}")
                    return False

            return result

    def get_track_segment_state(self, segment: TrackSegments) -> TrackSegmentState:
        """
        Get the track segment state.
        :param segment: The track segment to get the state of.
        : return: The state of the track segment (e.g., TrackSegmentState.FREE, TrackSegmentState.RESERVED, TrackSegmentState.OCCUPIED).
        """

        if panel_segments.segment_exists(segment):
            outputs: dict[str, OutputPort] = panel_segments.get_segment(segment)

            if outputs.get("occupied", None) and self.get_output(
                outputs.get("occupied", None)
            ):
                return TrackSegmentState.OCCUPIED

            elif outputs.get("reserved", None) and self.get_output(
                outputs.get("reserved", None)
            ):
                return TrackSegmentState.RESERVED

            elif outputs.get("building", None) and self.get_memory(
                outputs.get("building", None)
            ):
                return TrackSegmentState.BUILDING

            else:
                return TrackSegmentState.FREE

        return TrackSegmentState.OCCUPIED

    def read_database(self, location: DatabaseLocation, length: int = 1) -> bytearray:
        if location:
            return self.plc.db_read(int(location.value.replace("DB", "")), 0, length)
        return None

    def write_database(self, location: DatabaseLocation, data: bytearray, offset: int = 0) -> bool:
        if location:
            self.plc.db_write(int(location.value.replace("DB", "")), offset, data)
            return True
        return False

    def read_button_db(self, location: DatabaseLocation) -> ButtonDB:
        data: bytearray = self.read_database(location, 7)
        button_db = ButtonDB()
        button_db.button_press = (data[0] & 0b00000001) != 0
        button_db.button_pull = (data[0] & 0b00000010) != 0
        button_db.blink = (data[0] & 0b00000100) != 0

        button_db.indicator = (data[2] & 0b00000001) != 0
        button_db.VC_indicator = (data[4] & 0b00000001) != 0
        button_db.state = data[6]

        return button_db

    def write_button_db(self, location: DatabaseLocation, button_db: ButtonDB) -> bool:
        data = bytearray(7)
        data[0] = (
            (1 if button_db.button_press else 0)
            | (2 if button_db.button_pull else 0)
            | (4 if button_db.blink else 0)
        )
        data[2] = 1 if button_db.indicator else 0
        data[4] = 1 if button_db.VC_indicator else 0
        data[6] = button_db.state

        return self.write_database(location, data)
