from panel_interface.panel_interface import PanelInterface
from panel_interface.definitions.api_package import (
    DatabaseLocation,
    OutputPort,
    InputPort,
    TrackSegments,
    TrackSegmentState,
)

import logging
from time import sleep

logger = logging.getLogger("App.Test")
logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    panel = PanelInterface("192.168.1.2")
    panel.connect_plc()

    if panel.connected:
        for segment in TrackSegments:
            panel.set_track_segment(segment, TrackSegmentState.RESERVED)

    while panel.connected:
        vc: bool = False
        for btn in DatabaseLocation:
            if panel.read_button_db_field(btn, "VC_indicator"):
                vc = True

        panel.set_output(OutputPort.ROUTE_SELECTION, vc)

        if panel.get_input(InputPort.ROUTE_CANCEL) or panel.get_input(InputPort.ROUTE_OPTION_CANCEL):
            for btn in DatabaseLocation:
                res = panel.write_button_db_field(btn, "state", 0)
                if res is False:
                    logger.error(f"Failed to write ButtonDB at {btn.value}")

        sleep(0.5)
