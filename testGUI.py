#import section
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.buttom import Label

#app class

class HelloKivy(App):

    def build(self):
        return label(text="Hello Kivy")

helloKivy = HelloKivy()

helloKivy.run()
