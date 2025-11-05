from definitions.api_package import Signals, OutputPort


class PanelSignals:
    signal_dict: dict[Signals, dict[str, OutputPort]] = {
        Signals.L1: {
            "green": OutputPort.L1_0,
            "red": OutputPort.L1_1,
            "yellow": OutputPort.L1_2,
            "white": OutputPort.L1_3,
            "blue": OutputPort.L1_4,
        },
        Signals.L2: {},  # and so on for other signals
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
