# include path for /tools folder
import sys
import os.path
tool_dir = (os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..')) + '/tools/')
sys.path.append(tool_dir)

# import the required tools
from ADB_Action_Scipt import ActionScript
from RC_Code import SonyRCKey
from AppList import AppList
import Power_Tools as pt  # read Documentation for more info

# create an instance of the class, variables can be change
tv = ActionScript()  # if more than 1 device use: tv = ActionScript("Device ID")
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("Amazon is signed in")
print("Netflix is signed in")
print("Hulu is signed in")

# Print Instructions
print("What is does:")
print("Launch Netflix and play content")
print("Do trickplay every 5 minutes")
print("Launch Amazon and play content")
print("Do trickplay every 5 minutes")
print("Launch Hulu and play content")
print("Do trickplay every 5 minutes")


start = input("Press Enter to start")

# Automation Start
pt.trickplay_netflix(5, 6)


# ----------------------- Keep terminal open -----------------------------
close = input("Press Enter to close terminal")
