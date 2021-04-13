import argparse
import json


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



twitterPost.post(twitterJSON)


