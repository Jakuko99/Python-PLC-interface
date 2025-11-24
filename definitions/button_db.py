class ButtonDB:
    button_press: bool  # 0.0
    button_push: bool  # 0.1
    blink: bool  # 0.2

    indicator: bool  # 2.0
    VC_indicator: bool  # 4.0
    state: int  # 6.0

    def __str__(self):
        return (
            f"ButtonDB(button_press={self.button_press}, button_push={self.button_push}, "
            f"blink={self.blink}, indicator={self.indicator}, VC_indicator={self.VC_indicator}, "
            f"state={self.state})"
        )
