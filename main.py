from kivymd.app import MDApp

from app.utils.loader import load_kv_files
from app.screens.manager import AppManager


class PercentageApp(MDApp):

    def build(self):

        self.title = "Percentage App"

        self.theme_cls.primary_palette = "Blue"

        self.theme_cls.theme_style = "Light"

        load_kv_files()

        return AppManager()


if __name__ == "__main__":
    PercentageApp().run()