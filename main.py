from kivy.app import App
from screens.home import HomeScreen


class PercentageApp(App):

    def build(self):
        return HomeScreen()


PercentageApp().run()