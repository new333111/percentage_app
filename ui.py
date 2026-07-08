from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=20, **kwargs)

        self.amount = TextInput(
            hint_text="Amount",
            multiline=False,
            input_filter="float"
        )

        self.percent = TextInput(
            hint_text="Percentage",
            multiline=False,
            input_filter="float"
        )

        self.result = Label(
            text="Result: 0",
            font_size=24
        )

        btn = Button(
            text="Calculate",
            size_hint=(1, None),
            height=55
        )

        btn.bind(on_press=self.calculate)

        self.add_widget(self.amount)
        self.add_widget(self.percent)
        self.add_widget(btn)
        self.add_widget(self.result)

    def calculate(self, instance):
        try:
            amount = float(self.amount.text)
            percent = float(self.percent.text)

            value = amount * percent / 100

            self.result.text = f"Result: {value:.2f}"

        except ValueError:
            self.result.text = "Please enter valid numbers."