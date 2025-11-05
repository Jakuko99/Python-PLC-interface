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
)


class SegmentControl(QWidget):
    def __init__(self, segment: str, interface: PanelInterface, parent=None):
        super().__init__()
        self.parent = parent
        self.segment: str = segment
        self.interface: PanelInterface = interface

        self.state_choice = QComboBox(self)
        self.state_choice.addItems([state.name for state in TrackSegmentState])
        self.set_state_button = QPushButton("Set State", self)
        self.set_state_button.clicked.connect(self.set_segment_state)
        self.label = QLabel(f"{self.segment}", self)

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

        self.sign_choice = QComboBox(self)
        self.sign_choice.addItems([sign.name for sign in SignalSign])
        self.set_sign_button = QPushButton("Set Sign", self)
        self.set_sign_button.clicked.connect(self.set_signal_sign)
        self.label = QLabel(f"{self.signal}", self)

        self.lazy_layout = QVBoxLayout()
        self.lazy_layout.addWidget(self.label)
        self.lazy_layout.addWidget(self.sign_choice)
        self.lazy_layout.addWidget(self.set_sign_button)
        self.setLayout(self.lazy_layout)

    def set_signal_sign(self):
        selected_sign_name = self.sign_choice.currentText()
        selected_sign = SignalSign[selected_sign_name]

        self.interface.set_signal(Signals[self.signal], selected_sign)


class TestWindow(QMainWindow):
    def __init__(self, interface: PanelInterface):
        super().__init__()
        self.interface: PanelInterface = interface
        self.setWindowTitle("Track Segment and Signal Control")

        self.setCentralWidget(QWidget())
        layout = QGridLayout()
        row, column = 0, 0
        for segment in TrackSegments:
            layout.addWidget(
                SegmentControl(segment.name, self.interface, self), row, column
            )
            column += 1
            if column >= 15:
                column = 0
                row += 1

        for signal in Signals:
            layout.addWidget(
                SignalControl(signal.name, self.interface, self), row, column
            )
            column += 1
            if column >= 15:
                column = 0
                row += 1

        layout.addWidget(QPushButton("Connect PLC", self), row, column)
        layout.itemAtPosition(row, column).widget().clicked.connect(
            self.interface.connect_plc
        )
        self.centralWidget().setLayout(layout)


logger = logging.getLogger("App")
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    panel = PanelInterface("192.168.0.1")
    app = QApplication([])
    window = TestWindow(panel)

    window.show()
    app.exec_()
