# include path for /tools folder
import sys
import os.path
tool_dir = (os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..')) + '/tools/')
sys.path.append(tool_dir)

# First import the ADB_Action_Script.py it must be on the same folder
from ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from RC_Code import SonyRCKey
from AppList import AppList

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()


# ---------------------------Pre-built Functions HDMI--------------------------
def playback_hdmi(hdmi, time=0):
    """Launch selected HDMI and playback"""
    tv.press_rc_key(hdmi)
    tv.wait_in_minute(time)  # wait to load hdmi


def trickplay_hdmi(hdmi, time=10, loop=4):
    """Do channel change on HDMI with default value of 10min and 4 loops"""
    playback_hdmi(hdmi, time)
    # channel up
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_UP)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL UP loop count: {i}')
    # channel down
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_DOWN)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL DOWN loop count: {i}')


# ---------------------------Pre-built Functions Netflix--------------------------
def playback_netflix(time=0):
    """Launch Netflix then playback content based on given time"""
    tv.clear_launch_app(app.NETFLIX_PKG, app.NETFLIX_ACT)
    tv.wait_in_second(10)  # Wait load netflix
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(2)
    tv.press_rc_key(rc.DOWN)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


def trickplay_netflix(playback=2, speed=6):
    """ FF and RW speed is 10 seconds per second """
    playback_netflix()
    # trickplay starts
    tv.wait_in_minute(playback)
    tv.press_rc_key(rc.FF)
    tv.wait_in_second(speed)  # trickplay time
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(playback)  # playback time
    tv.press_rc_key(rc.RW)
    tv.wait_in_second(speed)  # trickplay time
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(playback)  # playback time


# ---------------------------Pre-built Functions Amazon--------------------------
def playback_amazon(time=0):
    """Launch Amazon then playback content based on given time"""
    tv.clear_launch_app(app.AMAZON_PKG, app.AMAZON_ACT)
    tv.wait_in_second(10)  # wait load amazon
    tv.press_rc_key(rc.DOWN)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


# ---------------------------Pre-built Functions Hulu--------------------------
def playback_hulu(time=0):
    """Launch Hulu then playback content based on given time"""
    tv.clear_launch_app(app.HULU_PKG, app.HULU_ACT)
    tv.wait_in_second(10)  # wait load hulu
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


# ---------------------------Pre-built Functions PSVue--------------------------
def playback_psvue(time=3):
    """Launch PSVue then playback content based on given time"""
    tv.clear_launch_app(app.PSVUE_PKG, app.PSVUE_ACT)
    tv.wait_in_second(10)  # wait to load psvue
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(10)  # wait to load playback
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


def trickplay_psvue(time=10, loop=4):
    """Do channel change on PS Vue with default value of 10min and 4 loops"""
    playback_psvue()
    # channel up loop
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_UP)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL UP loop count: {i}')
    # channel down loop
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_DOWN)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL UP loop count: {i}')
