# First import the ADB_Action_Script.py it must be on the same folder
from ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from RC_Code import SonyRCKey
from AppList import AppList
# include path for /tools folder
import sys
import os.path
tool_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) + '/tools/')
sys.path.append(tool_dir)

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()


# ---------------------------Pre-built Functions--------------------------
def trickplay_hdmi(hdmi, time=10, loop=4):
    """Do channel change on HDMI"""
    tv.press_rc_key(hdmi)
    tv.wait_in_second(5)
    # channel up
    for i in range(1, loop):
        tv.press_rc_key(rc.CHANNEL_UP)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL UP loop count: {i}')
    # channel down
    for i in range(1, loop):
        tv.press_rc_key(rc.CHANNEL_DOWN)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL DOWN loop count: {i}')


def playback_netflix(time):
    """Launch Netflix then playback content based on given time"""
    tv.clear_launch_app(app.NETFLIX_PKG, app.NETFLIX_ACT)
    tv.wait_in_second(8)  # Wait load netflix
    tv.press_rc_key(rc.NAV_ENTER)
    tv.wait_in_second(2)
    tv.press_rc_key(rc.NAV_DOWN)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.NAV_ENTER)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.NAV_ENTER)
    tv.wait_in_hour(time)  # playback time
    tv.press_rc_key(rc.HOME)
    tv.wait_in_second(5)


def playback_amazon(time):
    """Launch Amazon then playback content based on given time"""
    tv.clear_launch_app(app.AMAZON_PKG, app.AMAZON_ACT)
    tv.wait_in_second(8)  # wait load amazon
    tv.press_rc_key(rc.NAV_DOWN)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.NAV_ENTER)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.NAV_ENTER)
    tv.wait_in_hour(time)  # playback time
    tv.press_rc_key(rc.HOME)
    tv.wait_in_second(5)


def playback_hulu(time):
    """Launch Hulu then playback content based on given time"""
    tv.clear_launch_app(app.HULU_PKG, app.HULU_ACT)
    tv.wait_in_second(5)  # wait load hulu
    tv.press_rc_key(rc.NAV_ENTER)
    tv.wait_in_hour(time)  # playback time
