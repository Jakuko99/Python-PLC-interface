import s71200
import logging

from definitions.api_package import (
    InputPort,
    OutputPort,
    MemoryLocation,
    SignalSign,
    Signal,
    TrackSegmentState,
)
from panel_elements.api_package import panel_signals, panel_segments


class S7Interface(s71200.S71200):
    def __init__(self, ip: str, debug: bool = False):
        super.__init__(ip, debug)
        self.ip: str = ip
        self.logger = logging.getLogger("App.PLC_interface")
        self.logger.setLevel(logging.DEBUG)

        self.logger.info("PLC interface initalized")

    def connect_plc(self):
        self.connect()
        self.logger.debug(f"Connected to PLC at {self.ip}")

    def set_output(self, port: OutputPort, value: bool):
        pass

    def get_input(self, port: InputPort) -> bool:
        pass

    def set_memory(self, address: MemoryLocation, value: bool):
        pass

    def get_memory(self, address: MemoryLocation) -> bool:
        pass

    def set_signal(self, signal: Signal, sign: SignalSign) -> bool:
        """
        Set the signal value and sign.

        :param signal: The signal value to set.
        :param sign: The sign of the signal (e.g., SignalSign.STOP, SignalSign.FREE).
        """
        if panel_signals.signal_exists(signal):
            outputs: list[OutputPort] = panel_signals.get_signal(signal)

            for output in outputs:
                self.set_output(output, False)  # reset all outputs first

            match sign:  # TODO: neeeds to logic for several types of signals
                case SignalSign.STOP:
                    for output in outputs:
                        self.set_output(output, False)
                case SignalSign.FREE:
                    self.set_output(outputs[1], True)
                case SignalSign.SHUNT:
                    self.set_output(outputs[0], True)

            return True

        return False

    def get_signal_state(self, signal_name: str) -> SignalSign:
        pass
