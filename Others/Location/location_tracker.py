from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class Example(MDApp):
    def build(self):
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Pappulu", dp(30)),
                ("Oil", dp(30)),

            ],
            row_data=[
                (f"{i + 1}", "1", "2", "3", "4", "5") for i,j in range(50)
            ], check = True, background_color = [.10, 0.88, 0.9, .3]
        )

    def on_start(self):
        self.data_tables.open()


Example().run()