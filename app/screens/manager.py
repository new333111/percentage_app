from kivy.uix.screenmanager import ScreenManager, FadeTransition

from app.screens.home import HomeScreen


class AppManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.transition = FadeTransition()

        self.add_widget(HomeScreen())