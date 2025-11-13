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

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QComboBox,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QScrollArea,
)

from PyQt5.QtGui import QFont


class SegmentControl(QWidget):
    def __init__(self, segment: str, interface: PanelInterface, parent=None):
        super().__init__()
        self.parent = parent
        self.segment: str = segment
        self.interface: PanelInterface = interface

        font = QFont("Arial", 10)
        font.setBold(True)

        self.state_choice = QComboBox(self)
        self.state_choice.addItems([state.name for state in TrackSegmentState])
        self.set_state_button = QPushButton("Set State", self)
        self.set_state_button.clicked.connect(self.set_segment_state)
        self.label = QLabel(f"{self.segment}", self)
        self.label.setWordWrap(True)
        self.label.setFont(font)

        self.lazy_layout = QVBoxLayout()
        self.lazy_layout.addWidget(self.label)
        self.lazy_layout.addWidget(self.state_choice)
        self.lazy_layout.addWidget(self.set_state_button)
        self.setLayout(self.lazy_layout)

    def set_segment_state(self):
        selected_state_name = self.state_choice.currentText()
        selected_state = TrackSegmentState[selected_state_name]

        self.interface.set_track_segment(TrackSegments[self.segment], selected_state)


class SignalControl(QWidget):
    def __init__(self, signal: str, interface: PanelInterface, parent=None):
        super().__init__()
        self.parent = parent
        self.signal: str = signal
        self.interface: PanelInterface = interface

        font = QFont("Arial", 10)
        font.setBold(True)

        self.sign_choice = QComboBox(self)
        self.sign_choice.addItems([sign.name for sign in SignalSign])
        self.set_sign_button = QPushButton("Set Sign", self)
        self.set_sign_button.clicked.connect(self.set_signal_sign)
        self.label = QLabel(f"{self.signal}", self)
        self.label.setWordWrap(True)
        self.label.setFont(font)

        self.lazy_layout = QVBoxLayout()
        self.lazy_layout.addWidget(self.label)
        self.lazy_layout.addWidget(self.sign_choice)
        self.lazy_layout.addWidget(self.set_sign_button)
        self.setLayout(self.lazy_layout)

    def set_signal_sign(self):
        selected_sign_name = self.sign_choice.currentText()
        selected_sign = SignalSign[selected_sign_name]

        self.interface.set_signal(Signals[self.signal], selected_sign)


class OutputControl(QWidget):
    def __init__(self, output: str, interface: PanelInterface, parent=None):
        super().__init__()
        self.parent = parent
        self.output: str = output
        self.interface: PanelInterface = interface

        font = QFont("Arial", 10)
        font.setBold(True)

        self.turn_on_button = QPushButton("Turn on", self)
        self.turn_on_button.clicked.connect(lambda: self.set_output_state(True))
        self.turn_off_button = QPushButton("Turn off", self)
        self.turn_off_button.clicked.connect(lambda: self.set_output_state(False))
        self.label = QLabel(f"{self.output}", self)
        self.label.setWordWrap(True)
        self.label.setFont(font)

        self.lazy_layout = QVBoxLayout()
        self.lazy_layout.addWidget(self.label)
        self.lazy_layout.addWidget(self.turn_on_button)
        self.lazy_layout.addWidget(self.turn_off_button)
        self.setLayout(self.lazy_layout)

    def set_output_state(self, state: bool):

        self.interface.set_output(OutputPort[self.output], state)


class InputControl(QWidget):
    def __init__(self, input_port: str, interface: PanelInterface, parent=None):
        super().__init__()
        self.parent = parent
        self.input_port: str = input_port
        self.interface: PanelInterface = interface
        font = QFont("Arial", 10)
        font.setBold(True)
        self.label = QLabel(f"{self.input_port}", self)
        self.label.setWordWrap(True)
        self.label.setFont(font)
        self.button = QPushButton("Refresh Input", self)
        self.button.clicked.connect(self.refresh_input_state)
        self.lazy_layout = QVBoxLayout()
        self.lazy_layout.addWidget(self.label)
        self.lazy_layout.addWidget(self.button)
        self.setLayout(self.lazy_layout)

    def refresh_input_state(self):
        state = self.interface.get_input(InputPort[self.input_port])
        self.label.setText(f"{self.input_port}: {'ON' if state else 'OFF'}")


class TestWindow(QMainWindow):
    def __init__(self, interface: PanelInterface):
        super().__init__()
        self.interface: PanelInterface = interface
        self.setWindowTitle("Track Segment and Signal Control")

        self.setCentralWidget(QWidget())
        layout = QGridLayout()
        row, column = 0, 0

        layout.addWidget(QPushButton("Connect PLC", self), row, column)
        layout.itemAtPosition(row, column).widget().clicked.connect(
            self.interface.connect_plc
        )
        column += 1
        COLUMN_SIZE = 7

        for segment in TrackSegments:
            layout.addWidget(
                SegmentControl(segment.name, self.interface, self), row, column
            )
            column += 1
            if column >= COLUMN_SIZE:
                column = 0
                row += 1

        column, row = 0, row + 1
        for signal in Signals:
            layout.addWidget(
                SignalControl(signal.name, self.interface, self), row, column
            )
            column += 1
            if column >= COLUMN_SIZE:
                column = 0
                row += 1

        column, row = 0, row + 1
        for output in OutputPort:
            layout.addWidget(
                OutputControl(output.name, self.interface, self), row, column
            )
            column += 1
            if column >= COLUMN_SIZE:
                column = 0
                row += 1

        column, row = 0, row + 1
        for input_port in InputPort:
            layout.addWidget(
                InputControl(input_port.name, self.interface, self), row, column
            )
            column += 1
            if column >= COLUMN_SIZE:
                column = 0
                row += 1

        container = QWidget()
        container.setLayout(layout)
        scroll = QScrollArea()
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll)
        self.centralWidget().setLayout(main_layout)


logger = logging.getLogger("App")
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    panel = PanelInterface("1.1.1.2")
    app = QApplication([])
    window = TestWindow(panel)

    window.show()
    app.exec_()
