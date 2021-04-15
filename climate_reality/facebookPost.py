# This will assume that twitter is logged in for the account you want to post on
# When bluestacks is opened, it will be on its home page
import pyautogui
from pyscreeze import ImageNotFoundException
import subprocess
# Improting Image class from PIL module
from PIL import Image

import helper

FACEBOOK_IMAGE_SIZE = 400
MAX_IMAGES_FACEBOOK = 2
SCROLL_LENGTH = 300

PROFILE_LOCATION_X = 200

def CheckForImageQuantity(allLocations):
    if len(allLocations) > MAX_IMAGES_FACEBOOK:
        print("Too many Images")
        exit(1)

def GoToImportPage():
    helper.LocateAndClick('./common/home.png', helper.SMALL_PAUSE)
    helper.LocateAndClick('./common/application.png', helper.SMALL_PAUSE)
    helper.LocateAndClick('./common/settings.png', helper.MEDIUM_PAUSE)
    helper.LocateAndClick('./common/importImage.png', helper.SMALL_PAUSE)



def LeavePage():
    x, y = helper.LocateImage('./facebookImages/back.png')
    if x != None and y != None:
        helper.LocateAndClick('./facebookImages/back.png', helper.SMALL_PAUSE)
        helper.LocateAndClick('./facebookImages/home.png', helper.SMALL_PAUSE)


def GotToPage(username):
    helper.LocateAndClick('./facebookImages/menu.png', helper.MEDIUM_PAUSE)
    helper.LocateAndClick(username + "_facebook.png", helper.MEDIUM_PAUSE)

def post(inputJSON):
    assert "text" in inputJSON
    assert "type" in inputJSON
    
    


    # Open Application
    helper.LocateAndClick('./facebookImages/facebookLogo.png', helper.LARGE_PAUSE)
        
    LeavePage()
    
    GotToPage(inputJSON["user"])

    # Add Image from Windows
    if "images" in inputJSON:
        GoToImportPage()
        allLocations = inputJSON["images"]
        CheckForImageQuantity(allLocations)
        helper.AddAllImages(allLocations)
        helper.LocateAndClick('./common/home.png', helper.SMALL_PAUSE)
        helper.LocateAndClick('./facebookImages/facebookLogo.png', helper.MEDIUM_PAUSE)


    # Start Post
    helper.LocateAndClick('./facebookImages/create.png', helper.MEDIUM_PAUSE)
    
    
    # Attach Image
    if "images" in inputJSON:
        helper.LocateAndClick('./facebookImages/addPhoto.png', helper.MEDIUM_PAUSE)
        allImages = inputJSON["images"]
        for i, image in enumerate(allImages):            
            helper.LocateAndClick('./facebookImages/gallery.png', helper.MEDIUM_PAUSE, adjY = FACEBOOK_IMAGE_SIZE/2, adjX = (i+1)*FACEBOOK_IMAGE_SIZE)
        helper.LocateAndClick('./facebookImages/next.png', helper.MEDIUM_PAUSE)
    

        
  
    # Add text (Always at the end, else the links can change a lot of things
    helper.LocateAndClick('./facebookImages/text.png', helper.MEDIUM_PAUSE)    
    pyautogui.write(inputJSON["text"], interval = 0.1)


    # Tweet It Since its Ready
    helper.PauseForEffect(helper.WAIT_WINDOW)
    helper.LocateAndClick('./facebookImages/share.png', helper.MEDIUM_PAUSE)
    if inputJSON["type"] == "feed":
        helper.LocateAndClick('./facebookImages/feed.png', helper.SMALL_PAUSE)
    if inputJSON["type"] == "boost":
        helper.LocateAndClick('./facebookImages/boost.png', helper.SMALL_PAUSE)
    helper.LocateAndClick('./facebookImages/finalShare.png', helper.LARGE_PAUSE)
    
    
    helper.PauseForEffect(helper.SMALL_PAUSE)
    LeavePage()

    # Need to delete all the images from the Manager
    # Attach Image
    if "images" in inputJSON:
        # Add Image from Windows
        GoToImportPage()
        helper.LocateAndClick('./common/cancel.png', helper.SMALL_PAUSE)
        CheckForImageQuantity(inputJSON["images"])
        helper.DeleteAllImages(inputJSON["images"])
        helper.LocateAndClick('./common/home.png', helper.SMALL_PAUSE)
        


    
        
        
        
    
    
    
        
    