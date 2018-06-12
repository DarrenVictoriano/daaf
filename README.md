# Darren's AndroidTV Automation Framework

### What is it?
* This is a basically an Android ADB shell commands automated using python.
* Currently, the script only works on 1 device directly connected to the PC.
* This only have 2 functions right now; launch an app and send remote keycodes to the TV

### Requirements:
* Python 3 installed
* ADB installed and in the path
* Android TV

### How to use the scripts:
* Download or Clone Repository
* Select the script you to run on /DAAF/script/
* Read the each script's requirements
* Run python script (double click ".py" file)

### Create your own:
* First create a python file then import the following:
```
# First import the ADB_Action_Script.py it must be on the same folder
from tools.ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from tools.RC_Code import SonyRCKey
from tools.AppList import AppList
```
* Second, Create an instalce of the classes
```
# variables can be changed
tv = ActionScript()
rc = SonyRCKey()
app = AppList()
```
* Check "Sample_Script.py" for an example

## Documentation:
Below are the core functions from the ActionScript() class.

**launch_app(app_pkg)** - takes one argument; the application's package you want to launch. This will launch the app using monkey tool. Does not force stop the app, it will resume previous activity if the app had been launch before.
*(you can get the app's pkg from AppLists() class)*

**clear_launch_app(app_pkg, app_activity)** - takes two arguments; the application's package and activity you want to launch. This will force stop the app first then launch it. This will allow you to launch the app from the initial state always.
*(you can get the app's pkg & activity from AppLists() class)*

**press_rc_key(rc_codes)** - takes one argument; the remote control's key code. This will send keyevent using adb.
*(you can get sony remote key codes from SonyRCKey() class)*

**wait_in_second(seconds)** - takes one argument; any floating point numbers representing a "second". This will pause the script base on the given time.

**wait_in_minute(minutes)** - takes one argument; any floating point numbers representing a "minute". This will pause the script base on the given time.

**wait_in_hour(hours)** - takes one argument; any floating point numbers representing an "hour". This will pause the script base on the given time.

___
Below are the pre-made functions from the Power_Tools module for easy coding.

**trickplay_hdmi(hdmi, time=10, loop=4)** - takes 3 arguments; 1st the HDMI input from RC_codes, then time in minutes and 3rd how many loops. This will tune to \<HDMI\> you set then change channel change every \<time you set\> and will repeat depending on how many \<loop\> you specify

**playback_netflix(time)** - take 1 argument; playback time in minutes, it can me integer or floating point. This will launch Netflix, select 1st profile and play the 1st content it focuses and will continue playback depending on the \<time\> you set.

**playback_amazon(time)** - take 1 argument; playback time in minutes, it can me integer or floating point. This will launch Amazon, select 1st profile and play the 1st content it focuses and will continue playback depending on the \<time\> you set.

**playback_hulu(time)** - take 1 argument; playback time in minutes, it can me integer or floating point. This will launch Hulu, select 1st profile and play the 1st content it focuses and will continue playback depending on the \<time\> you set.
