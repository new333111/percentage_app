from kivy.app import App
from screens.manager import AppManager


class PercentageApp(App):

    def build(self):
        return AppManager()


PercentageApp().run()