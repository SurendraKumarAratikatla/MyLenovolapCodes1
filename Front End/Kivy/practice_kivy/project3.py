from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string('''

#:import Label kivy.uix.label.Label

GridLayout:
    cols: 3
    on_parent:
        for i in range(10): txt = "Label {0}".format(i); self.add_widget(Label(text = txt, text_size=(cm(2), cm(2)), pos=self.pos,
        id=txt, color=(1,1,1,1)))
'''))