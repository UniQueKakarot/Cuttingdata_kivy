
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class ToolMonitor(BoxLayout):

    def __init__(self, tab_controll, **kwargs):
        super(ToolMonitor, self).__init__(**kwargs)

        self.master = tab_controll

        test = GridLayout(cols=1, spacing=1, padding=10)

        for i in range(11):
            test.add_widget(Label(text=f'Test{i+1}', font_size=20))

        test2 = GridLayout(cols=1, spacing=7, padding=10, size_hint_y=None)
        test2.bind(minimum_height=test2.setter('height'))

        for i in range(100):
            test2.add_widget(Label(text=f"Tool{i+1}", size_hint_y=None, height=20))
        
        scroll_test = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 55))
        scroll_test.add_widget(test2)

        self.add_widget(test)
        self.add_widget(scroll_test)

        self.master.add_widget(self)
