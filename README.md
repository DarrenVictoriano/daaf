# Darren's AndroidTV Automation Framework

What is it?
* This is a basically an Android ADB shell commands automated using python.
* Currently, the script only works on 1 device directly connected to the PC.
* This only have 2 functions right now; launch an app and send remote keycodes to the TV

Requirements:
* Python 3 installed
* ADB installed and in the path
* Android TV

How to use the scripts:
* Download or Clone Repository
* Select script to run /DAAF/script/
* Run python script

Create your own:
* Create a python file then import the following:
    >>>
    from tools.ADB_Action_Scipt import ActionScript
    from tools.RC_Code import SonyRCKey
    from tools.AppList import AppLists
