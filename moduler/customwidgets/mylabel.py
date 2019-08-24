from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<MyLabel>:
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")


class MyLabel(Label):
    bcolor = ListProperty([1, 1, 1, 1])


Factory.register('KivyB', module='MyLabel')
