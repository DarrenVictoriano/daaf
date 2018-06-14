# Sony TV Automation Scripts

This is a collection of test Automation Script for Sony Android TV
* Each folder is a test script with its own unique requirements and test
* Follow all requirements in the description before running the script

How to make your own:
* First you need Python 3 installed
* Second ADB installed and in the path
* Lastly Android TV

How to use:
* Create a folder inside /DAAF/scripts/
* Your folder should contain the python script and a README.md file
* README.md file is a text file that should contain the requirements and description of the script
* Before writing your code; your script should have the following imports (see -=template=- folder):
```
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
import Power_Tools as pt
```
