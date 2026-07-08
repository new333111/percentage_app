from kivy.clock import Clock
from kivymd.uix.screen import MDScreen

from app.config import Config


class SplashScreen(MDScreen):

    def on_enter(self, *args):
        """
        يتم استدعاؤها عند دخول شاشة البداية.
        """
        Clock.schedule_once(self.goto_home, Config.SPLASH_TIME)

    def goto_home(self, dt):
        """
        الانتقال إلى الشاشة الرئيسية.
        """
        self.manager.current = "home"