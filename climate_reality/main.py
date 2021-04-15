import argparse
import json
import pywinauto


import helper
import twitterPost
import linkedInPost
import facebookPost

parser = argparse.ArgumentParser()
parser.add_argument('-linkedin',
                    type=str,
                    help='LinkedIn JSON', required = False)
parser.add_argument('-facebook',
                    type=str,
                    help='Facebook JSON', required = False)
parser.add_argument('-twitter',
                    type=str,
                    help='Twitter JSON', required = False)
args = parser.parse_args()


twitterJSON = {}
if args.twitter is not None:
    try:
        with open(args.twitter, "r") as f:
            twitterJSON = json.load(f)
    except OSError:
        print("File Read Error")
    helper.PrettyPrintJSON(twitterJSON)


linkedinJSON = {}
if args.linkedin is not None:
    try:
        with open(args.linkedin, "r") as f:
            linkedinJSON = json.load(f)
    except OSError:
        print("File Read Error")
    helper.PrettyPrintJSON(linkedinJSON)

facebookJSON = {}
if args.facebook is not None:
    try:
        with open(args.facebook, "r") as f:
            facebookJSON = json.load(f)
    except OSError:
        print("File Read Error")
    helper.PrettyPrintJSON(facebookJSON)


# Import pywinauto Application class
from pywinauto.application import Application
# Start a new process and specify a path to the text file
app = Application().start('C:/Program Files/BlueStacks_arabica/HD-Player.exe --vmname Nougat32', timeout=helper.WAIT_WINDOW)


# helper.PauseForEffect(helper.WAIT_WINDOW)
helper.PauseForEffect(helper.SMALL_PAUSE)
dlg_spec = app.window()


# Resize the window
x, y = helper.LocateImage('./common/restore.png')
if x != None and y != None:
    helper.LocateAndClick('./common/restore.png', helper.SMALL_PAUSE)
helper.LocateAndClick('./common/maximize.png', helper.SMALL_PAUSE)


# twitterPost.post(twitterJSON)
# linkedInPost.post(linkedinJSON)
facebookPost.post(facebookJSON)


