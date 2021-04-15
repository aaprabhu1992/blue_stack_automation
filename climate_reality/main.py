import argparse
import json
import pywinauto


import helper
import twitterPost

parser = argparse.ArgumentParser()
# parser.add_argument('-instagram',
                    # type=str,
                    # help='Instagram JSON')
parser.add_argument('-twitter',
                    type=str,
                    help='Twitter JSON')
args = parser.parse_args()
twitterJSON = {}
try:
    with open(args.twitter, "r") as f:
        twitterJSON = json.load(f)
except OSError:
    print("File Read Error")
helper.PrettyPrintJSON(twitterJSON)
helper.PauseForEffect(5)

# Import pywinauto Application class
from pywinauto.application import Application
# Start a new process and specify a path to the text file
app = Application().start('C:/Program Files/BlueStacks_arabica/HD-Player.exe --vmname Nougat32', timeout=helper.WAIT_WINDOW)
helper.PauseForEffect(helper.WAIT_WINDOW)
dlg_spec = app.window()


# Resize the window
x, y = helper.LocateImage('./common/restore.png')
if x != None and y != None:
    helper.LocateAndClick('./common/restore.png', helper.SMALL_PAUSE)
helper.LocateAndClick('./common/maximize.png', helper.SMALL_PAUSE)


twitterPost.post(twitterJSON)


