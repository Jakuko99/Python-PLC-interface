import s71200
import logging

from definitions.api_package import InputPort, OutputPort, MemoryLocation, SignalSign

class S7Interface(s71200.S71200):
    def __init__(self, ip: str, debug: bool = False):
        super.__init__(ip, debug)
        self.ip :str = ip
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

    def set_memory(self, address: MemoryLocation, value : bool):
        pass

    def get_memory(self, address: MemoryLocation) -> bool:
        pass

    def set_signal(self, signal_name: str, sign: SignalSign):
        pass

    def get_signal_state(self, signal_name: str) -> SignalSign:
        pass