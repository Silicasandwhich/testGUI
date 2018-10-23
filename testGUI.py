#import section
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.stacklayout import StackLayout

#app class

class StackLayoutApp(App):

    def build(self):
        return StackLayout()

slApp = StackLayoutApp()

slApp.run()
