from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15


        title = Label(
            text="Percentage Calculator",
            font_size=30
        )


        self.amount_input = TextInput(
            hint_text="Enter amount",
            multiline=False,
            input_filter="float"
        )


        self.percent_input = TextInput(
            hint_text="Enter percentage",
            multiline=False,
            input_filter="float"
        )


        calculate_btn = Button(
            text="Calculate",
            size_hint=(1, 0.3)
        )

        calculate_btn.bind(
            on_press=self.calculate
        )


        self.result = Label(
            text="Result: 0",
            font_size=24
        )


        self.add_widget(title)
        self.add_widget(self.amount_input)
        self.add_widget(self.percent_input)
        self.add_widget(calculate_btn)
        self.add_widget(self.result)



    def calculate(self, instance):

        try:
            amount = float(self.amount_input.text)
            percent = float(self.percent_input.text)

            result = amount * percent / 100

            self.result.text = f"Result: {result}"

        except:
            self.result.text = "Invalid input"