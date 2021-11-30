from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class CautionPanelScreen(Screen):
    pass
class TextScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen):
        # get the screen manager from the main.kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen

    def get_text(self, caution):
        text_label = self.root.ids['text_screen'].ids['text_label']
        caution_open = open(caution, 'r')
        text_label.text = caution_open.read()

MainApp().run()

