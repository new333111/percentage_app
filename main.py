from kivymd.app import MDApp
from screens.manager import AppManager


class PercentageApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        return AppManager()


PercentageApp().run()