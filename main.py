from kivy.app import App
from ui import MainUI


class PercentageApp(App):

    def build(self):
        self.title = "Percentage Calculator"
        return MainUI()


if __name__ == "__main__":
    PercentageApp().run()