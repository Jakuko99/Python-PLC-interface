import logging

from S7_interface.panel_interface import PanelInterface
from S7_interface.definitions.api_package import (
    OutputPort,
    Signals,
    SignalSign,
    TrackSegmentState,
    InputPort,
    TrackSegments,
)

logger = logging.getLogger("App")
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    panel = PanelInterface("1.1.1.2")
    if panel.connect_plc():
        print("PLC connected successfully.")

    if panel.connected:
        for signal in Signals:
            if panel.set_signal(signal, SignalSign.FREE) is False:
                panel.set_signal(signal, SignalSign.SHUNT)

        for segment in TrackSegments:
            panel.set_track_segment(segment, TrackSegmentState.RESERVED)
