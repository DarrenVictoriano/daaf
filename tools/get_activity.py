# First import the ADB_Action_Script.py it must be on the same folder
from DAAF.ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from DAAF.ADB_Action_Scipt import SonyRCKey
from DAAF.ADB_Action_Scipt import AppLists

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppLists()

# Script Instructions
print("This will try to get the MainActivity of an app")
tv.get_activity_mfocus()
