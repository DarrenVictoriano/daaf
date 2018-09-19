# Darren's AndroidTV Automation Framework

### What is it:
* This is a basically an Android ADB shell commands automated using python.
* Check Documentation below.

### Requirements:
* Python 3 installed and in the path
* ADB installed and in the path
* Android TV

### How to use the pre-made scripts:
* Download or Clone Repository
* Select the script you to run on /DAAF/script/
* Read the each script's requirements
* Run python script (double click ".py" file)

### Create your own:
* Just download the "/tools" folder and import the required tools
    * First create a python file then import the following:
        ```
        # First import the ADB_Action_Script.py it must be on the same folder
        from tools.ADB_Action_Scipt import ActionScript
        # then import the RC keys and App PKGs for easy scripting
        from tools.RC_Code import SonyRCKey
        from tools.AppList import AppList
        import Power_Tools as pt
        ```
    * Second, Create an instance of the classes.
        ```
        # if there is only 1 device connected
        tv = ActionScript()
        rc = SonyRCKey()
        app = AppList()

        ```
        if multiple device connected, test specific device using device ID or ip address of the device
        ```
        # device ID or IP address should be inside a quotation
        tv = ActionScript("device ID or IP address")
        rc = SonyRCKey()
        app = AppList()

        ```
    * Check "Sample_Script.py" for an example
* Note: the only difference between creating script from root directory and "/DAAF/script" folder is the import statement

## Documentation:
Below are the core functions from the **ActionScript()** class. Following the imports above this is how to use the ActionScript() class; example "*tv.launch_app(app.NETFLIX_PKG)*"

**launch_app(app_pkg)** - takes one argument; the application's package you want to launch. This will launch the app using monkey tool. Does not force stop the app, it will resume previous activity if the app had been launch before.
*(you can get the app's pkg from AppLists() class)*

**clear_launch_app(app_pkg, app_activity)** - takes two arguments; the application's package and activity you want to launch. This will force stop the app first then launch it. This will allow you to launch the app from the initial state always.
*(you can get the app's pkg & activity from AppLists() class)*

**press_rc_key(rc_codes)** - takes one argument; the remote control's key code. This will send keyevent using adb.
*(you can get sony remote key codes from SonyRCKey() class)*

**wait_in_second(seconds)** - takes one argument; any floating point numbers representing a "second". This will pause the script base on the given time.

**wait_in_minute(minutes)** - takes one argument; any floating point numbers representing a "minute". This will pause the script base on the given time.

**wait_in_hour(hours)** - takes one argument; any floating point numbers representing an "hour". This will pause the script base on the given time.

**get_activity_mfocus()** - this will print the package and activity of the app in the terminal, first launch the app on the TV then run the get_activity.py

___
Below are functions from **Power_Tools** module. Example "*pt.trickplay_hdmi(rc.HDMI1, 5, 2)*"

**playback_netflix(time)** - take 1 argument; playback time in minutes, it can me integer or floating point. This will launch Netflix, select 1st profile and play the 1st content it focuses and will continue playback depending on the \<time\> you set.

**playback_amazon(time)** - take 1 argument; playback time in minutes, it can me integer or floating point. This will launch Amazon, select 1st profile and play the 1st content it focuses and will continue playback depending on the \<time\> you set.

**playback_hulu(time)** - take 1 argument; playback time in minutes, it can me integer or floating point. This will launch Hulu, select 1st profile and play the 1st content it focuses and will continue playback depending on the \<time\> you set.

**trickplay_hdmi(hdmi, time=10, loop=4)** - takes 3 arguments; 1st the HDMI input from RC_codes, then time in minutes and 3rd how many loops. This will tune to \<HDMI\> you set then change channel change every \<time you set\> and will repeat depending on how many \<loop\> you specify. (Default value of 10min and 4 loops)

**trickplay_psvue(time=10, loop=4)** - takes 2 arguments; time in minutes and how many loops. This will launch PS Vue then change channel change every \<time you set\> and will repeat depending on how many \<loop\> you specify. (Default value of 10min and 4 loops)

___
Below are the list of **SonyRCKey()**, Concatinate with RC instance to use it. Example "*rc.POWER*"
```
POWER - Press Power key
INPUT - Press Inpout  key
BRAIVA_SYNC_MENU - Press Sync Menu key
STB_MENU - Press STB Menu key

NUMBER_0 - Press 0
NUMBER_1 - Press 1
NUMBER_2 - Press 2
NUMBER_3 - Press 3
NUMBER_4 - Press 4
NUMBER_5 - Press 5
NUMBER_6 - Press 6
NUMBER_7 - Press 7
NUMBER_8 - Press 8
NUMBER_9 - Press 9
DOT - Press (.)

GOOGLE_PLAY - Press Google Play key
NETFLIX - Press Netflix key
YOUTUBE - Press YouTube key
YELLOW - Press Yellow key
BLUE - Press Blue key
RED - Press Red key
GREEN - Press Green key

ACTION_MENU - Press Action Menu key
GUIDE - Press Guide key
APPS - Press Apps key
BACK - Press Back key
HOME - Press Home key
TV - Press TV key

UP - Press Up key
DOWN - Press Down key
LEFT - Press Left key
RIGHT - Press Right key
ENTER - Press Enter key

VOLUME_UP - Press Volume Up key
VOLUME_DOWN - Press Volume Down key
JUMP - Press Jump key
MUTE - Press Mute key
CHANNEL_UP - Press Channel Up key
CHANNEL_DOWN - Press Channel Down key

AUDIO - Press Audio key
FF - Press Fast Forward key
PLAY - Press Play key
RW - Press Rewind key
SUBTITLE - Press CC/Close caption key
PREV - Press Previous key
PAUSE - Press Pause key
NEXT - Press Next key
HELP - Press Help key
WIDE - Press Wide Mode key
STOP - Press Stop key

HDMI1 - Tune to HDMI1
HDMI2 - Tune to HDMI2
HDMI3 - Tune to HDMI3
HDMI4 - Tune to HDMI4
VIDEO - Tune to Video
```

___
Below are the list of **AppList()**, Concatinate with AppList instance to use it. Example "*app.NETFLIX_PKG or app.NETFLIX_ACT*"
```
NETFLIX_PKG - Netflix Package Name
AMAZON_PKG - Amazon Package Name
HULU_PKG - Hulu Package Name
YOUTUBE_PKG - YouTube Package Name
VUDU_PKG - Vudu Package Name
SETTINGS_PKG - Settings Package Name
PSVUE_PKG - PS Vue Package Name
```
```
NETFLIX_ACT - Netflix Activity Name
AMAZON_ACT - Amazon Activity Name
HULU_ACT - Hulu Activity Name
YOUTUBE_ACT - YouTube Activity Name
VUDU_ACT - Vudu Activity Name
SETTINGS_ACT - Settings Activity Name
PSVUE_ACT - PS Vue Activity Name
```
