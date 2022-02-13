import time
from classes.ZoomMeeting import ZoomMeeting
from classes.JWLibrary import JWLibrary

zoom_meeting = ZoomMeeting()
jw_library = JWLibrary()

zoom_meeting.enter_meeting()
time.sleep(10)
jw_library.open_jw_library()
