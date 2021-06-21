"""
Create a MDApp, add one Screen and load from file given as parameter
example call: compare README.md
links:
https://kivy.org/doc/stable/api-kivy.config.html
"""
import argparse
import os

# os.environ["KIVY_NO_CONSOLELOG"] = "1"
os.environ["KCFG_KIVY_LOG_LEVEL"] = "error"

from kivy.config import Config
Config.set("graphics", "resizable", 0)  # only works if used before window is created, i.e. before importing kivy stuff

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window


class MyScreen(Screen):
    pass


class ShowScreenApp(MDApp):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MyScreen(name='Test'))
        return manager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str, help="name of the .kv file to load")
    parser.add_argument("--height", type=int, default=1920//3)
    parser.add_argument("--width", type=int, default=1080//3)
    args = parser.parse_args()

    file_path = os.path.join("screens", args.file_name)

    if not os.path.exists(file_path):
        print("ERROR no file named {} in directory {}".format(args.file_name, "screens"))
        exit(1)

    Window.size = (args.width, args.height)
    Config.set("kivy", "log_level", "warning")

    Builder.load_file(file_path)

    ShowScreenApp().run()


if __name__ == '__main__':
    main()
