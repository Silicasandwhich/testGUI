#import section
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

#app class

class FloatingApp(App):

    def build(self):
        return FLoatLayout()

flApp = FloatingApp()

flApp.run()
