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
import Power_Tools as pt  # this is for pre-made functions. read Documentation for more info

# create an instance of the class, variables can be change
tv = ActionScript()  # if more than 1 device use: tv = ActionScript("Device ID")
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("HDMI1 with IRBlaster setup")
print("Amazon, Netflix, Hulu and Vudu are signed in")
print("Auto program completed for RF\n")

# Print Instructions
print("This is what the script does:")
print("Launch Hulu for 1 hour")
print("Launch Netflix for 1 hour")
print("Launch Amazon for 1 hour")
print("Tune back to HDMI1 for 1 hour")
print("Power OFF TV")

start = input("Press Enter to start script")

# Automation Start
# ------------------------------- Hulu ----------------------------------
tv.clear_launch_app(app.HULU_PKG, app.HULU_ACT)
tv.wait_in_second(8)  # wait load hulu
tv.press_rc_key(rc.ENTER)
tv.wait_in_hour(1)  # playback time

# ------------------------------- Netflix ---------------------------------
tv.clear_launch_app(app.NETFLIX_PKG, app.NETFLIX_ACT)
tv.wait_in_second(8)  # wait netflix to load
tv.press_rc_key(rc.ENTER)
tv.wait_in_second(2)
tv.press_rc_key(rc.DOWN)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)  # playback start
tv.wait_in_minute(1)
tv.press_rc_key(rc.HOME)
tv.wait_in_second(5)

# ------------------------------- Amazon ---------------------------------
tv.clear_launch_app(app.AMAZON_PKG, app.AMAZON_ACT)
tv.wait_in_second(8)  # wait amazon to load
tv.press_rc_key(rc.DOWN)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)  # playback start
tv.wait_in_second(5)
tv.press_rc_key(rc.HOME)
tv.wait_in_second(5)

# RC OFF TV
tv.press_rc_key(rc.POWER)

# ------------------------- Keep terminal open -----------------------------
close = input("Press Enter to close terminal")
