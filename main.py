import kivy as kv
import random as rd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput




class FirstLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #btn_1 = Button(text="just a button", color=(0, 0, 255))
        #btn_2 = Button(text="just a button", color=(255, 0, 0))
        #self.add_widget(btn_1)
        #self.add_widget(btn_2)

    def test_foo(self):
        #text = self.ids.text_in.text
        #print(text)
        pass

class MainWidget(Widget):
    pass

class TheLabelApp(App):
    def build(self):
        #Window.clearcolor = (1, 1, 1, 1)
        return FirstLayout()

if __name__ == "__main__":
    app = TheLabelApp().run()