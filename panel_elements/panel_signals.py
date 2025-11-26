from panel_interface.definitions.api_package import Signals, OutputPort, MemoryLocation


class PanelSignals:
    signal_dict: dict[Signals, dict[str, OutputPort]] = {
        Signals.PR_L: {"green": OutputPort.PR_L_GREEN},
        Signals.L: {
            "green": OutputPort.L_GREEN,
            "yellow": OutputPort.L_YELLOW,
            "red": OutputPort.L_RED,
            "white": OutputPort.L_WHITE,
            "white_blink": MemoryLocation.L_WHITE_BLINK,
            "memory": MemoryLocation.N_L,
        },
        Signals.SE1: {"white": OutputPort.SE1_WHITE},
        Signals.S1: {
            "green": OutputPort.S1_GREEN,
            "white": OutputPort.S1_WHITE,
            "white_blink": MemoryLocation.S1_WHITE_BLINK,
            "memory": MemoryLocation.N_S1,
        },
        Signals.S2: {
            "green": OutputPort.S2_GREEN,
            "white": OutputPort.S2_WHITE,
            "white_blink": MemoryLocation.S2_WHITE_BLINK,
            "memory": MemoryLocation.N_S2,
        },
        Signals.S3: {
            "green": OutputPort.S3_GREEN,
            "white": OutputPort.S3_WHITE,
            "white_blink": MemoryLocation.S3_WHITE_BLINK,
            "memory": MemoryLocation.N_S3,
        },
        Signals.S4: {
            "green": OutputPort.S4_GREEN,
            "white": OutputPort.S4_WHITE,
            "white_blink": MemoryLocation.S4_WHITE_BLINK,
            "memory": MemoryLocation.N_S4,
        },
        Signals.SE2: {"white": OutputPort.SE2_WHITE},
        Signals.SE3: {"white": OutputPort.SE3_WHITE},
        Signals.L1: {
            "green": OutputPort.L1_GREEN,
            "white": OutputPort.L1_WHITE,
            "yellow": OutputPort.L1_YELLOW,
            "white_blink": MemoryLocation.L1_WHITE_BLINK,
            "memory": MemoryLocation.N_L1,
        },
        Signals.L2: {
            "green": OutputPort.L2_GREEN,
            "white": OutputPort.L2_WHITE,
            "yellow": OutputPort.L2_YELLOW,
            "white_blink": MemoryLocation.L2_WHITE_BLINK,
            "memory": MemoryLocation.N_L2,
        },
        Signals.L3: {
            "green": OutputPort.L3_GREEN,
            "white": OutputPort.L3_WHITE,
            "yellow": OutputPort.L3_YELLOW,
            "white_blink": MemoryLocation.L3_WHITE_BLINK,
            "memory": MemoryLocation.N_L3,
        },
        Signals.L4: {
            "green": OutputPort.L4_GREEN,
            "white": OutputPort.L4_WHITE,
            "yellow": OutputPort.L4_YELLOW,
            "white_blink": MemoryLocation.L4_WHITE_BLINK,
            "memory": MemoryLocation.N_L4,
        },
        Signals.SE4: {"white": OutputPort.SE4_WHITE},
        Signals.SE5: {"white": OutputPort.SE5_WHITE},
        Signals.SE6: {"white": OutputPort.SE6_WHITE},
        Signals._1S: {
            "green": OutputPort._1S_GREEN,
            "yellow": OutputPort._1S_YELLOW,
            "red": OutputPort._1S_RED,
            "white": OutputPort._1S_WHITE,
            "white_blink": MemoryLocation._1S_WHITE_BLINK,
            "memory": MemoryLocation.N_1S,
        },
        Signals._2S: {
            "green": OutputPort._2S_GREEN,
            "yellow": OutputPort._2S_YELLOW,
            "red": OutputPort._2S_RED,
            "white": OutputPort._2S_WHITE,
            "white_blink": MemoryLocation._2S_WHITE_BLINK,
            "memory": MemoryLocation.N_2S,
        },
        Signals._1_24: {"green": OutputPort._1_24_GREEN},
        Signals._2_24: {"green": OutputPort._2_24_GREEN},
    }

    def signal_exists(self, signal: Signals) -> bool:
        """
        Check if the signal exists in the signal dictionary.

        :param signal: The signal to check.
        :return: True if the signal exists, False otherwise.
        """
        return signal in self.signal_dict

    def get_signal(self, signal: Signals) -> dict[str, OutputPort]:
        """
        Get the list of output ports associated with the signal.

        :param signal: The signal to get.
        :return: A list of output ports associated with the signal.
        """
        return self.signal_dict.get(signal, {})


panel_signals = PanelSignals()
