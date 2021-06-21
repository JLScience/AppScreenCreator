# App Screen Creator

This project has the purpose to provide a minimalistic app skeleton using a screen.

With that, screens used in other applications can be created and tested 
using the kivy design language without implementing any logic.

The app requires python3, and the following packages installed:

kivy
kivymd

To run the app, create a .kv file in the screens/ directory and run the following command from the base directory:

python3 main.py <KIVY_FILE_NAME>

You can also change the screen size (e.g. to match another devices format):

python3 main.py <KIVY_FILE_NAME> --height 1234 --width 555
