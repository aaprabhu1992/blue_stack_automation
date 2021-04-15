import json
import time
import pyautogui

MIN_SLEEP_TIME = 10


SMALL_PAUSE = 3
MEDIUM_PAUSE = 10
LARGE_PAUSE = 20    
WAIT_WINDOW = 40

def PrettyPrintJSON(jsonObj, jsonIndent = 3):
    print(json.dumps(jsonObj, indent = jsonIndent))


def PauseForEffect(inputTime):
    while inputTime > 10:
        time.sleep(MIN_SLEEP_TIME)
        inputTime -= 10
        print("Waited for 10 sec, Time Left: {}".format(inputTime))
    time.sleep(inputTime)




def LocateImage(templateImageLocation, confidence_input = 0.9):
    x = None
    y = None
    try:
        x, y = pyautogui.locateCenterOnScreen(templateImageLocation, grayscale = True, confidence= confidence_input)
        print("Button FOUND : {}".format(templateImageLocation))
    except:
        print("Button not Found : {}".format(templateImageLocation))
    return x, y
def ClickAndWait(x,y, waitTime = 0):
    if x != None and y != None:
        pyautogui.click(x,y)
        if waitTime > 0:
            PauseForEffect(waitTime)
    else:
        exit(1)

def LocateAndClick(templateImageLocation, waitTime = 0, adjX = 0, adjY = 0, confidence_input = 0.9):
    x, y = LocateImage(templateImageLocation, confidence_input)
    ClickAndWait(x + adjX, y + adjY, waitTime)



def AddAllImages(allLocations):
    for i, imagePath in enumerate(allLocations):
        imagePath = imagePath.replace("/", "\\")
        if i == 0:
            pyautogui.write(imagePath, interval = 0.1)
            LocateAndClick('./twitterImages/open.png', SMALL_PAUSE)
        else:
            LocateAndClick('./twitterImages/importImageMore.png', SMALL_PAUSE)
            pyautogui.write(imagePath, interval = 0.1)
            LocateAndClick('./twitterImages/open.png', SMALL_PAUSE)


def DeleteAllImages(allLocations):
    LocateAndClick('./twitterImages/appMedia.png', SMALL_PAUSE, adjX = 700)
    totalLength = len(allLocations)
    for i, imagePath in enumerate(allLocations):
        LocateAndClick('./twitterImages/home.png', MEDIUM_PAUSE, adjX = 1130, adjY = 1470)
