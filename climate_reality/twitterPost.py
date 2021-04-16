# This will assume that twitter is logged in for the account you want to post on
# When bluestacks is opened, it will be on its home page
import pyautogui
from pyscreeze import ImageNotFoundException
import subprocess
# Improting Image class from PIL module
from PIL import Image

import helper

TWITTER_CHAR_LIMIT = 280
TWITTER_IMAGE_SIZE = 400
MAX_IMAGES_TWITTER = 5
TAG_GAP = 20
BANNER_GAP = 50
SCROLL_LENGTH = 300

PROFILE_LOCATION_X = 1250
CURRENTLY_WORKING = True

def CheckForImageQuantity(allLocations):
    if len(allLocations) > MAX_IMAGES_TWITTER:
        print("Too many Images")
        exit(1)

            
            
def AttachAllImages(allLocations):
    if len(allLocations) > MAX_IMAGES_TWITTER:
        print("Too many Images")
        exit(1)
    totalLength = len(allLocations)
    for i, imagePath in enumerate(allLocations):
        helper.LocateAndClick('./twitterImages/addImageButton.png', helper.SMALL_PAUSE)
        if i == 0:
            helper.LocateAndClick('./twitterImages/camera.png', helper.SMALL_PAUSE, adjX = (totalLength - i)*TWITTER_IMAGE_SIZE)
        else:
            helper.LocateAndClick('./twitterImages/camera.png', helper.SMALL_PAUSE, adjX = (totalLength - i)*TWITTER_IMAGE_SIZE)
            helper.LocateAndClick('./twitterImages/add.png', helper.SMALL_PAUSE)




def DetectLocationActive():
    locationPath = './twitterImages/addLocationButton.png'
    x, y = helper.LocateImage(locationPath)
    if x != None and y != None:
        return locationPath
    else:
        locationPath = './twitterImages/addLocationFilledButton.png'
        x, y = helper.LocateImage(locationPath)
        if x != None and y != None:
            return locationPath
    return ''
    
def SwitchUser(username):
    helper.LocateAndClick('./twitterImages/homepageBird.png', helper.SMALL_PAUSE, adjX = -PROFILE_LOCATION_X)
    helper.LocateAndClick('./twitterImages/multipleProfile.png', helper.SMALL_PAUSE)
    helper.LocateAndClick(username + "_twitter.png", helper.MEDIUM_PAUSE)
    
def post(inputJSON):
    assert "text" in inputJSON
    assert len(inputJSON["text"]) <= 280
    
    


    # Open Application
    helper.LocateAndClick('./twitterImages/twitterLogo.png', helper.LARGE_PAUSE)
    
    helper.PauseForEffect(3)
    # Switch user
    SwitchUser(inputJSON["user"])
    # Start Tweet
    helper.LocateAndClick('./twitterImages/tweetButton.png', helper.MEDIUM_PAUSE)
    
    
    # Add Location first, else it reads from the Image
    if "location" in inputJSON:
        locationActive = DetectLocationActive()
        helper.LocateAndClick(locationActive, helper.SMALL_PAUSE)
        helper.PauseForEffect(helper.LARGE_PAUSE)
        helper.LocateAndClick('./twitterImages/searchLocation.png', helper.SMALL_PAUSE)
        pyautogui.write(inputJSON["location"], interval = 0.1)
        pyautogui.press('enter')
        helper.PauseForEffect(helper.LARGE_PAUSE)
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.scroll(-SCROLL_LENGTH)


    # Attach Image
    if "images" in inputJSON:
        # Add Image from Windows
        helper.GoToImportPage()
        allLocations = inputJSON["images"]
        CheckForImageQuantity(allLocations)
        helper.AddAllImages(allLocations)
        helper.LocateAndClick('./common/home.png', helper.SMALL_PAUSE)
        # Attach Image
        helper.LocateAndClick('./twitterImages/twitterLogo.png', helper.MEDIUM_PAUSE)
        AttachAllImages(allLocations)
        pyautogui.scroll(-SCROLL_LENGTH)
        helper.PauseForEffect(helper.SMALL_PAUSE)
        
    # Add Tags    
    if "images" in inputJSON and "tags" in inputJSON:
        tagClick = ('./twitterImages/tag_1.png', './twitterImages/tag_many.png')[len(inputJSON["images"]) > 1]
        x, y = helper.LocateImage(tagClick)
        if x != None and y != None:
            helper.LocateAndClick(tagClick, helper.SMALL_PAUSE)
            allTags = inputJSON["tags"]
            x = None
            y = None
            for i, tagValue in enumerate(allTags):
                if i == 0:
                    x, y = helper.LocateImage('./twitterImages/tagSearch.png')
                    # helper.ClickAndWait(x,y, helper.SMALL_PAUSE)
                    # pyautogui.write(tagValue, interval = 0.1)
                    # helper.ClickAndWait(x,y + (i+1)*TAG_GAP, helper.SMALL_PAUSE)
                # else:
                helper.ClickAndWait(x,y, helper.SMALL_PAUSE)
                pyautogui.press('esc')
                pyautogui.press('enter')
                pyautogui.write(tagValue, interval = 0.1)
                helper.PauseForEffect(helper.SMALL_PAUSE)
                xTag, yTag = helper.LocateImage('./twitterImages/tagLine.png')
                helper.ClickAndWait(xTag, yTag + BANNER_GAP/2, helper.SMALL_PAUSE)
            helper.LocateAndClick('./twitterImages/done.png', helper.SMALL_PAUSE)
        else:
            print("Tagging not Possible")
  
    # Add text (Always at the end, else the links can change a lot of things
    pyautogui.write(inputJSON["text"], interval = 0.1)


    # Tweet It Since its Ready
    helper.PauseForEffect(helper.WAIT_WINDOW)
    helper.LocateAndClick('./twitterImages/tweet.png', helper.WAIT_WINDOW)
    
    
    helper.PauseForEffect(helper.SMALL_PAUSE)
    # Need to delete all the images from the Manager
    # Attach Image
    if "images" in inputJSON:
        # Add Image from Windows
        helper.GoToImportPage()
        helper.LocateAndClick('./common/cancel.png', helper.SMALL_PAUSE)
        CheckForImageQuantity(inputJSON["images"])
        helper.DeleteAllImages(inputJSON["images"])
        helper.LocateAndClick('./common/home.png', helper.SMALL_PAUSE)


        
        
        
    
    
    
        
    