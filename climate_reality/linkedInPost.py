# This will assume that twitter is logged in for the account you want to post on
# When bluestacks is opened, it will be on its home page
import pyautogui
from pyscreeze import ImageNotFoundException
import subprocess
# Improting Image class from PIL module
from PIL import Image

import helper

LINKEDIN_IMAGE_SIZE = 400
MAX_IMAGES_LINKEDIN = 1
SCROLL_LENGTH = 300

PROFILE_LOCATION_X = 200

def CheckForImageQuantity(allLocations):
    if len(allLocations) > MAX_IMAGES_LINKEDIN:
        print("Too many Images")
        exit(1)

                
def SignInUser(inputJSON):
    helper.LocateAndClick(inputJSON["user"] + "_linkedin.png", helper.LARGE_PAUSE)
    helper.LocateAndClick('./linkedinImages/search.png', helper.SMALL_PAUSE, adjX = -PROFILE_LOCATION_X)
    if "page" in inputJSON:
        helper.LocateAndClick(inputJSON["page"] + "_linkedin_page.png", helper.MEDIUM_PAUSE)


def SignOutUser():
    helper.LocateAndClick('./linkedinImages/search.png', helper.SMALL_PAUSE, adjX = -PROFILE_LOCATION_X)
    helper.LocateAndClick('./linkedinImages/settings.png', helper.MEDIUM_PAUSE)
    pyautogui.scroll(-SCROLL_LENGTH)
    helper.PauseForEffect(helper.MEDIUM_PAUSE)
    helper.LocateAndClick('./linkedinImages/signOut.png', helper.MEDIUM_PAUSE)


def LeavePage():
    x, y = helper.LocateImage('./linkedinImages/back.png')
    if x != None and y != None:
        helper.LocateAndClick('./linkedinImages/back.png', helper.SMALL_PAUSE)

def RemoveStickers():
    x, y = helper.LocateImage('./linkedinImages/sticker.png')
    if x != None and y != None:
        helper.LocateAndClick('./linkedinImages/sticker.png', helper.SMALL_PAUSE, adjY = -LINKEDIN_IMAGE_SIZE/2)


def SignOutPreviousUser():
    x, y = helper.LocateImage('./linkedinImages/search.png')
    if x != None and y != None:
        SignOutUser()

def post(inputJSON):
    assert "text" in inputJSON
    
    


    # Open Application
    helper.LocateAndClick('./linkedinImages/linkedinLogo.png', helper.LARGE_PAUSE)
    
    helper.PauseForEffect(3)
    
    LeavePage()
    SignOutPreviousUser()
    # Switch user
    SignInUser(inputJSON)

    # Add Image from Windows
    if "images" in inputJSON:
        helper.GoToImportPage()
        allLocations = inputJSON["images"]
        CheckForImageQuantity(allLocations)
        helper.AddAllImages(allLocations)
        helper.LocateAndClick('./common/home.png', helper.SMALL_PAUSE)
        helper.LocateAndClick('./linkedinImages/linkedinLogo.png', helper.MEDIUM_PAUSE)


    # Start Post
    helper.LocateAndClick('./linkedinImages/post.png', helper.MEDIUM_PAUSE)
    
    
    # Attach Image
    if "images" in inputJSON:
        helper.LocateAndClick('./linkedinImages/addPhoto.png', helper.MEDIUM_PAUSE)
        helper.LocateAndClick('./linkedinImages/recent.png', helper.MEDIUM_PAUSE, adjY = LINKEDIN_IMAGE_SIZE/2)
        RemoveStickers()
        helper.LocateAndClick('./linkedinImages/continue.png', helper.MEDIUM_PAUSE)
    

        
  
    # Add text (Always at the end, else the links can change a lot of things
    pyautogui.write(inputJSON["text"], interval = 0.1)


    # Tweet It Since its Ready
    helper.PauseForEffect(helper.WAIT_WINDOW)
    helper.LocateAndClick('./linkedinImages/postButton.png', helper.WAIT_WINDOW)
    
    
    helper.PauseForEffect(helper.SMALL_PAUSE)
    helper.LocateAndClick('./linkedinImages/back.png', helper.MEDIUM_PAUSE)
    
    SignOutUser()

    # Need to delete all the images from the Manager
    # Attach Image
    if "images" in inputJSON:
        # Add Image from Windows
        helper.GoToImportPage()
        helper.LocateAndClick('./common/cancel.png', helper.SMALL_PAUSE)
        CheckForImageQuantity(inputJSON["images"])
        helper.DeleteAllImages(inputJSON["images"])
        helper.LocateAndClick('./common/home.png', helper.SMALL_PAUSE)
        


    
        
        
        
    
    
    
        
    