from kivymd.app import MDApp

from app.config import Config
from app.utils.loader import load_kv_files
from app.screens.manager import AppManager


class AndroidTemplateApp(MDApp):

    def build(self):

        load_kv_files()

        self.title = Config.APP_NAME

        self.theme_cls.primary_palette = Config.PRIMARY_PALETTE

        self.theme_cls.theme_style = Config.THEME_STYLE

        return AppManager()


if __name__ == "__main__":
    AndroidTemplateApp().run()