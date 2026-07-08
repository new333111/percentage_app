from kivy.app import App
from ui import MainLayout


class PercentageApp(App):
    def build(self):
        self.title = "Percentage Calculator"
        return MainLayout()


if __name__ == "__main__":
    PercentageApp().run()