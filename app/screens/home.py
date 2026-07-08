from kivy.uix.screenmanager import Screen
from services.calculator import Calculator


class HomeScreen(Screen):

    def calculate(self):

        try:
            amount = float(self.ids.amount.text)
            percent = float(self.ids.percent.text)

            result = Calculator.percentage(amount, percent)

            self.ids.result.text = f"Result: {result:.2f}"

        except ValueError:
            self.ids.result.text = "Invalid Input"