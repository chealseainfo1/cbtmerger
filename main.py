from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class FrontPageScreen(Screen):
    pass

class TileCalculatorScreen(Screen):
    def calculate_tiles(self):
        try:
            length = float(self.ids.length_input.text)
            width = float(self.ids.width_input.text)
            tile_len_cm = float(self.ids.tile_len_input.text)
            tile_wid_cm = float(self.ids.tile_wid_input.text)
            per_carton = int(self.ids.tiles_per_carton_input.text)

            tile_len = tile_len_cm / 100
            tile_wid = tile_wid_cm / 100

            adj_area = (length + 0.1) * (width + 0.1)
            tile_area = tile_len * tile_wid

            # Calculate tiles needed without using math.ceil
            tiles_needed = int(adj_area / tile_area)
            if adj_area / tile_area > tiles_needed:
                tiles_needed += 1

            cartons_needed = int(tiles_needed / per_carton)
            if tiles_needed / per_carton > cartons_needed:
                cartons_needed += 1

            self.ids.result_label.text = (
                f"Adjusted floor area: {adj_area:.2f} sqm\n"
                f"Tile area: {tile_area:.2f} sqm\n"
                f"Tiles needed: {tiles_needed}\n"
                f"Cartons needed: {cartons_needed}"
            )
        except Exception as e:
            self.ids.result_label.text = f"Error: {str(e)}"

    def clear_inputs(self):
        self.ids.length_input.text = ""
        self.ids.width_input.text = ""
        self.ids.tile_len_input.text = ""
        self.ids.tile_wid_input.text = ""
        self.ids.tiles_per_carton_input.text = ""
        self.ids.result_label.text = ""

# KV string remains the same
kv = """
ScreenManager:
    FrontPageScreen:
    TileCalculatorScreen:

<FrontPageScreen>:
    name: 'front'
    canvas.before:
        Color:
            rgba: (0.1, 0.1, 0.6, 0.6)   # blue background
        Rectangle:
            size: self.size
            pos: self.pos

    GridLayout:
        rows: 3
        cols: 1
        Label:
            text: "APPLICATION OF SURFACE AREA \\nIN BUILDING CONSTRUCTION"
            font_size: 30
            markup: True

        Label:
            text: "Joseph Oluwatobi Isaac (SCI20MTH043)\\nSupervisor: Mr. E. C. Akaligwo"
            font_size: 28
            markup: True

        Button:
            text: 'Continue'
            font_size: 30
            size_hint_y: None
            height: '48dp'
            on_release: app.root.current = 'calc'

<TileCalculatorScreen>:
    name: 'calc'
    canvas.before:
        Color:
            rgba: (0.1, 0.1, 0.6, 0.6)
        Rectangle:
            size: self.size
            pos: self.pos

    GridLayout:
        rows: 7
        cols: 2
        padding: 10
        spacing: 10

        Label:
            text: 'Floor length (m):'
        TextInput:
            id: length_input
            multiline: False
            input_filter: 'float'

        Label:
            text: 'Floor width (m):'
        TextInput:
            id: width_input
            multiline: False
            input_filter: 'float'

        Label:
            text: 'Tile length (cm):'
        TextInput:
            id: tile_len_input
            multiline: False
            input_filter: 'float'

        Label:
            text: 'Tile width (cm):'
        TextInput:
            id: tile_wid_input
            multiline: False
            input_filter: 'float'

        Label:
            text: 'Tiles per carton:'
        TextInput:
            id: tiles_per_carton_input
            multiline: False
            input_filter: 'int'

        Label:
            text: 'Result:'
        Label:
            id: result_label
            text: ''
            text_size: self.size
            valign: 'top'
            halign: 'left'
            height: self.texture_size[1]
            color: (0, 0, 0, 1)
            canvas.before:
                Color:
                    rgba: (1, 1, 1, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos

        Button:
            text: 'Calculate'
            on_release: root.calculate_tiles()
        Button:
            text: 'Clear'
            on_release: root.clear_inputs()
"""

Builder.load_string(kv)

class TileCalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FrontPageScreen(name='front'))
        sm.add_widget(TileCalculatorScreen(name='calc'))
        sm.current = 'front'
        return sm

if __name__ == "__main__":
    TileCalculatorApp().run()
