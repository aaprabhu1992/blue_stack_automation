# This will assume that twitter is logged in for the account you want to post on
# When bluestacks is opened, it will be on its home page
import pyautogui
import pywinauto
from pyscreeze import ImageNotFoundException
import subprocess
# Improting Image class from PIL module
from PIL import Image

import helper

TWITTER_CHAR_LIMIT = 280
WAIT_WINDOW = 40
TWITTER_IMAGE_SIZE = 400
MAX_IMAGES = 5
TAG_GAP = 20
BANNER_GAP = 50
SCROLL_LENGTH = 300

SMALL_PAUSE = 3
MEDIUM_PAUSE = 10
LARGE_PAUSE = 20    


CURRENTLY_WORKING = True


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
            helper.PauseForEffect(waitTime)
    else:
        exit(1)

def LocateAndClick(templateImageLocation, waitTime = 0, adjX = 0, adjY = 0, confidence_input = 0.9):
    x, y = LocateImage(templateImageLocation, confidence_input)
    ClickAndWait(x + adjX, y + adjY, waitTime)

def AddAllImages(allLocations):
    if len(allLocations) > MAX_IMAGES:
        print("Too many Images")
        exit(1)
    for i, imagePath in enumerate(allLocations):
        imagePath = imagePath.replace("/", "\\")
        if i == 0:
            pyautogui.write(imagePath, interval = 0.1)
            LocateAndClick('./twitterImages/open.png', SMALL_PAUSE)
        else:
            LocateAndClick('./twitterImages/importImageMore.png', SMALL_PAUSE)
            pyautogui.write(imagePath, interval = 0.1)
            LocateAndClick('./twitterImages/open.png', SMALL_PAUSE)
            
            
def AttachAllImages(allLocations):
    if len(allLocations) > MAX_IMAGES:
        print("Too many Images")
        exit(1)
    totalLength = len(allLocations)
    for i, imagePath in enumerate(allLocations):
        LocateAndClick('./twitterImages/addImageButton.png', SMALL_PAUSE)
        if i == 0:
            LocateAndClick('./twitterImages/camera.png', SMALL_PAUSE, adjX = (totalLength - i)*TWITTER_IMAGE_SIZE)
        else:
            LocateAndClick('./twitterImages/camera.png', SMALL_PAUSE, adjX = (totalLength - i)*TWITTER_IMAGE_SIZE)
            LocateAndClick('./twitterImages/add.png', SMALL_PAUSE)

def DeleteAllImages(allLocations):
    if len(allLocations) > MAX_IMAGES:
        print("Too many Images")
        exit(1)
    LocateAndClick('./twitterImages/appMedia.png', SMALL_PAUSE, adjX = 700)
    totalLength = len(allLocations)
    for i, imagePath in enumerate(allLocations):
        LocateAndClick('./twitterImages/home.png', MEDIUM_PAUSE, adjX = 1130, adjY = 1470)



def DetectLocationActive():
    locationPath = './twitterImages/addLocationButton.png'
    x, y = LocateImage(locationPath)
    if x != None and y != None:
        return locationPath
    else:
        locationPath = './twitterImages/addLocationFilledButton.png'
        x, y = LocateImage(locationPath)
        if x != None and y != None:
            return locationPath
    return ''
def post(inputJSON):
    assert "text" in inputJSON
    assert len(inputJSON["text"]) <= 280
    
    
    # Import pywinauto Application class
    from pywinauto.application import Application
    # Start a new process and specify a path to the text file
    app = Application().start('C:/Program Files/BlueStacks_arabica/HD-Player.exe --vmname Nougat32', timeout=WAIT_WINDOW)
    helper.PauseForEffect(WAIT_WINDOW)
    dlg_spec = app.window()


    # Resize the window
    x, y = LocateImage('./twitterImages/restore.png')
    if x != None and y != None:
        LocateAndClick('./twitterImages/restore.png', SMALL_PAUSE)
    LocateAndClick('./twitterImages/maximize.png', SMALL_PAUSE)


    # Open Application
    LocateAndClick('./twitterImages/twitterLogo.png', LARGE_PAUSE)
    
    # Start Tweet
    LocateAndClick('./twitterImages/tweetButton.png', MEDIUM_PAUSE)
    
    
    # Add Location first, else it reads from the Image
    if "location" in inputJSON:
        locationActive = DetectLocationActive()
        LocateAndClick(locationActive, SMALL_PAUSE)
        helper.PauseForEffect(LARGE_PAUSE)
        LocateAndClick('./twitterImages/searchLocation.png', SMALL_PAUSE)
        pyautogui.write(inputJSON["location"], interval = 0.1)
        pyautogui.press('enter')
        helper.PauseForEffect(LARGE_PAUSE)
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.scroll(-SCROLL_LENGTH)


    # Attach Image
    if "images" in inputJSON:
        # Add Image from Windows
        LocateAndClick('./twitterImages/home.png', SMALL_PAUSE)
        LocateAndClick('./twitterImages/application.png', SMALL_PAUSE)
        LocateAndClick('./twitterImages/settings.png', MEDIUM_PAUSE)
        LocateAndClick('./twitterImages/importImage.png', SMALL_PAUSE)
        allLocations = inputJSON["images"]
        AddAllImages(allLocations)
        LocateAndClick('./twitterImages/home.png', SMALL_PAUSE)
        # Attach Image
        LocateAndClick('./twitterImages/twitterLogo.png', MEDIUM_PAUSE)
        AttachAllImages(allLocations)
        pyautogui.scroll(-SCROLL_LENGTH)
        helper.PauseForEffect(SMALL_PAUSE)
        
    # Add Tags    
    if "images" in inputJSON and "tags" in inputJSON:
        tagClick = ('./twitterImages/tag_1.png', './twitterImages/tag_many.png')[len(inputJSON["images"]) > 1]
        LocateAndClick(tagClick, SMALL_PAUSE)
        allTags = inputJSON["tags"]
        x = None
        y = None
        for i, tagValue in enumerate(allTags):
            if i == 0:
                x, y = LocateImage('./twitterImages/tagSearch.png')
                # ClickAndWait(x,y, SMALL_PAUSE)
                # pyautogui.write(tagValue, interval = 0.1)
                # ClickAndWait(x,y + (i+1)*TAG_GAP, SMALL_PAUSE)
            # else:
            ClickAndWait(x,y, SMALL_PAUSE)
            pyautogui.press('esc')
            pyautogui.press('enter')
            pyautogui.write(tagValue, interval = 0.1)
            helper.PauseForEffect(SMALL_PAUSE)
            xTag, yTag = LocateImage('./twitterImages/tagLine.png')
            ClickAndWait(xTag, yTag + BANNER_GAP/2, SMALL_PAUSE)
        LocateAndClick('./twitterImages/done.png', SMALL_PAUSE)
  
    # Add text (Always at the end, else the links can change a lot of things
    pyautogui.write(inputJSON["text"], interval = 0.1)


    # Tweet It Since its Ready
    helper.PauseForEffect(WAIT_WINDOW)
    LocateAndClick('./twitterImages/tweet.png', WAIT_WINDOW)
    
    
    helper.PauseForEffect(SMALL_PAUSE)
    # Need to delete all the images from the Manager
    # Attach Image
    if "images" in inputJSON:
        # Add Image from Windows
        LocateAndClick('./twitterImages/home.png', SMALL_PAUSE)
        LocateAndClick('./twitterImages/application.png', SMALL_PAUSE)
        LocateAndClick('./twitterImages/settings.png', MEDIUM_PAUSE)
        LocateAndClick('./twitterImages/importImage.png', SMALL_PAUSE)
        LocateAndClick('./twitterImages/cancel.png', SMALL_PAUSE)
        DeleteAllImages(inputJSON["images"])
        LocateAndClick('./twitterImages/home.png', SMALL_PAUSE)


        
        
        
    
    
    
        
    