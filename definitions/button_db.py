class ButtonDB:
    button_press: bool = False  # 0.0
    button_pull: bool = False  # 0.1
    blink: bool = False  # 0.2

    indicator: bool = False  # 2.0
    VC_indicator: bool = False  # 4.0
    state: int = 0  # 6.0

    def __str__(self):
        return (
            f"ButtonDB(button_press={self.button_press}, button_push={self.button_pull}, "
            f"blink={self.blink}, indicator={self.indicator}, VC_indicator={self.VC_indicator}, "
            f"state={self.state})"
        )
