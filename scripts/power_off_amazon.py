# First import the ADB_Action_Script.py it must be on the same folder
from DAAF.ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from DAAF.ADB_Action_Scipt import SonyRCKey
from DAAF.ADB_Action_Scipt import AppLists

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppLists()

# Print Requirements
print("Requirements:")
print("HDMI1 with IRBlaster setup")
print("Amazon, Netflix, Hulu and Vudu are signed in")
print("Auto program completed for RF\n")

# Print Instructions
print("This is what the script does:")
print("Tune to HDMI1 for 1 hour")
print("Then change channel every 10 minutes")
print("Launch Netflix for 1 hour")
print("Launch Amazon for 1 hour")
print("Tune back to HDMI1 for 1 hour")
print("Power OFF TV")


# Automation Start
# ------------------------------- HDMI1 ----------------------------------
tv.press_rc_key(rc.TUNE_HDMI1)
tv.wait_in_seconds(5)
# channel up
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_UP)
    tv.wait_in_seconds(5)
    print(f'CHANNEL UP loop count: {i}')
# channel down
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_DOWN)
    tv.wait_in_seconds(5)
    print(f'CHANNEL DOWN loop count: {i}')

# ------------------------------- Netflix ---------------------------------
tv.clear_launch_app(app.NETFLIX_PKG, app.NETFLIX_ACT)
tv.wait_in_seconds(8)
tv.press_rc_key(rc.NAV_ENTER)
tv.wait_in_seconds(2)
tv.press_rc_key(rc.NAV_DOWN)
tv.wait_in_seconds(1.5)
tv.press_rc_key(rc.NAV_ENTER)
tv.wait_in_seconds(1.5)
tv.press_rc_key(rc.NAV_ENTER) # playback start
tv.wait_in_minute(1)
tv.press_rc_key(rc.HOME)
tv.wait_in_seconds(5)

# ------------------------------- Amazon ---------------------------------
tv.clear_launch_app(app.AMAZON_PKG, app.AMAZON_ACT)
tv.wait_in_seconds(8)
tv.press_rc_key(rc.NAV_DOWN)
tv.wait_in_seconds(1.5)
tv.press_rc_key(rc.NAV_ENTER)
tv.wait_in_seconds(1.5)
tv.press_rc_key(rc.NAV_ENTER) # playback start
tv.wait_in_seconds(5)
tv.press_rc_key(rc.HOME)
tv.wait_in_seconds(5)

# RC OFF TV
tv.press_rc_key(rc.POWER)

# ------------------------------- Keep terminal open ---------------------------------
close = input("Press Enter to close terminal")
