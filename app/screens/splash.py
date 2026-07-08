from kivymd.uix.screen import MDScreen
from kivy.clock import Clock


class SplashScreen(MDScreen):

    def on_enter(self, *args):
        Clock.schedule_once(self.goto_home, 2)

    def goto_home(self, dt):
        self.manager.current = "home"