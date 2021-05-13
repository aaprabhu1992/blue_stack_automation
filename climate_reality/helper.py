import json
import time
import pyautogui

MIN_SLEEP_TIME = 10


SMALL_PAUSE = 3
MEDIUM_PAUSE = 10
LARGE_PAUSE = 20    
WAIT_WINDOW = 40


def Scroll(distance, occurence):
    for i in range(0,occurence):
        pyautogui.scroll(distance)



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

def GoToImportPage():
    LocateAndClick('./common/home.png', SMALL_PAUSE)
    LocateAndClick('./common/application.png', SMALL_PAUSE)
    LocateAndClick('./common/settings.png', MEDIUM_PAUSE)
    LocateAndClick('./common/importImage.png', SMALL_PAUSE)


def AddAllImages(allLocations):
    for i, imagePath in enumerate(allLocations):
        imagePath = imagePath.replace("/", "\\")
        if i == 0:
            pyautogui.write(imagePath, interval = 0.1)
            LocateAndClick('./common/open.png', SMALL_PAUSE)
        else:
            LocateAndClick('./common/importImageMore.png', SMALL_PAUSE)
            pyautogui.write(imagePath, interval = 0.1)
            LocateAndClick('./common/open.png', SMALL_PAUSE)


def DeleteAllImages(allLocations):
    LocateAndClick('./common/appMedia.png', SMALL_PAUSE, adjX = 700)
    totalLength = len(allLocations)
    for i, imagePath in enumerate(allLocations):
        LocateAndClick('./common/home.png', MEDIUM_PAUSE, adjX = 1130, adjY = 1470)
