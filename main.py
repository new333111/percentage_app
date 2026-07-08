from kivymd.app import MDApp

from app.config import Config
from app.utils.loader import load_kv_files
from app.screens.manager import AppManager


class AndroidTemplateApp(MDApp):

    def build(self):
        # تحميل جميع ملفات KV
        load_kv_files()

        # معلومات التطبيق
        self.title = Config.APP_NAME

        # إعداد الثيم
        self.theme_cls.theme_style = Config.THEME_STYLE
        self.theme_cls.primary_palette = Config.PRIMARY_PALETTE

        # إنشاء مدير الشاشات
        return AppManager()


if __name__ == "__main__":
    AndroidTemplateApp().run()