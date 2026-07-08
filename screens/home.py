from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):

    def calculate(self):

        try:
            amount = float(self.ids.amount.text)
            percent = float(self.ids.percent.text)

            result = amount * percent / 100

            self.ids.result.text = f"Result : {result:.2f}"

        except ValueError:
            self.ids.result.text = "Invalid Input"