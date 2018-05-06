import ADB_Action_Scipt as AScript  # This is where all the actions are
import TV_App_Packages as TvApp  # This is a list of TV App PKG name
import Sony_Remote_Keycodes as RCKey  # This is a list of Sony remote key codes


AScript.launch_app(TvApp.NETFLIX)  # launch netflix
AScript.wait_a_sec(2)  # wait 2 seconds, if left blank it will wait 1 sec
AScript.press_rc_key(RCKey.POWER)  # RC OFF TV (NOTE: key presses pauses 500ms automatically)
