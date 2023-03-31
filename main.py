import kivy as kv
import random as rd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button




class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        """btn_1 = Button(text="just a button", color=(0, 0, 255))
        btn_2 = Button(text="just a button", color=(255, 0, 0))
        self.add_widget(btn_1)
        self.add_widget(btn_2)"""
    
    def hello_world(self):
        print("hello world")



class MainWidget(Widget):
    pass


class TheLabelApp(App):
    def build(self):
        return BoxLayoutExample()

if __name__ == "__main__":
    app = TheLabelApp().run()