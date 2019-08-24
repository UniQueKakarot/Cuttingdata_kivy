from kivy.uix.textinput import TextInput


class MyTextInput(TextInput):

    def on_focus(self, instance, value):
        if value:
            self.text = ""
