from definitions.api_package import Signal, OutputPort


class PanelSignals:
    signal_dict: dict[Signal, list[OutputPort]] = {
        Signal.L1: [
            OutputPort.L1_0,
            OutputPort.L1_1,
        ],
        Signal.L2: [],  # and so on for other signals
    }

    def signal_exists(self, signal: Signal) -> bool:
        """
        Check if the signal exists in the signal dictionary.

        :param signal: The signal to check.
        :return: True if the signal exists, False otherwise.
        """
        return signal in self.signal_dict

    def get_signal(self, signal: Signal) -> list[OutputPort]:
        """
        Get the list of output ports associated with the signal.

        :param signal: The signal to get.
        :return: A list of output ports associated with the signal.
        """
        return self.signal_dict.get(signal, [])


panel_signals = PanelSignals()
