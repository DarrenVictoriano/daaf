class AppList:
    """A list of activities and packages of android app"""

    def __init__(self):
        """initialize app pkgs and activities"""
        # List of app pkgs
        self.NETFLIX_PKG = "com.netflix.ninja"
        self.AMAZON_PKG = "com.amazon.amazonvideo.livingroom"
        self.HULU_PKG = "com.hulu.livingroomplus"
        self.YOUTUBE_PKG = "com.google.android.youtube.tv"
        self.VUDU_PKG = "air.com.vudu.air.DownloaderTablet"
        self.SETTINGS_PKG = "com.android.tv.settings"
        self.PSVUE_PKG = "com.snei.vue.atv"

        # List of app app_activity
        self.NETFLIX_ACT = "com.netflix.ninja.MainActivity"
        self.AMAZON_ACT = "com.amazon.ignition.IgnitionActivity"
        self.HULU_ACT = "com.hulu.livingroomplus.MainActivity"
        self.YOUTUBE_ACT = "com.google.android.apps.youtube.tv.cobalt.activity.ShellActivity"
        self.VUDU_ACT = "com.vudu.android.app.activities.NavigationListActivity"
        self.SETTINGS_ACT = "com.sony.dtv.settings.MainSettings"
        self.PSVUE_ACT = "com.snei.vue.ui.MainActivity"
