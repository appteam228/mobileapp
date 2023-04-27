from kivymd.app import MDApp
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton, MDRoundFlatButton



KV = """
<MainDemoScreen>:

    MDFillRoundFlatButton:
        set_radius: 12
        set_color: (0, 1, 1, 1)

    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton"
        icon: "language-python"
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": .5, "center_y": .5}    

"""
class Main_Screen(MDScreen):
    pass
class Box_Layout(MDBoxLayout):
    pass

class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.layout_1 = Box_Layout()
        self.screen = Main_Screen()
        icon_button_1 = MDIconButton(
            icon = "instrument-triangle.png",
            icon_size = "64sp",
            line_width = 1,
            md_bg_color = (121, 34, 12, 0),
            icon_color = (0, 121, 12)
            
        )
        rounded_button_1 = MDRoundFlatButton(
            text = "Here is just demo",
            text_color = (12/255, 123, 12, 0)
        )

        self.layout_1.add_widget(icon_button_1)
        self.layout_1.add_widget(rounded_button_1)
        self.screen.add_widget(self.layout_1)
        return self.screen


if __name__ == "__main__":
    DemoApp().run()
