import json
import time

MIN_SLEEP_TIME = 10
def PrettyPrintJSON(jsonObj, jsonIndent = 3):
    print(json.dumps(jsonObj, indent = jsonIndent))


def PauseForEffect(inputTime):
    while inputTime > 10:
        time.sleep(MIN_SLEEP_TIME)
        inputTime -= 10
        print("Waited for 10 sec, Time Left: {}".format(inputTime))
    time.sleep(inputTime)
    
    