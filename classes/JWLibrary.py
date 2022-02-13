import time
import pyautogui

class JWLibrary:
  def __init__(self):
    pass

  def open_start_menu(self):
    pyautogui.press("win")

  def click_on_jw_library(self):
    pyautogui.click(363, 667)

  def open_jw_library(self):
    self.open_start_menu()
    time.sleep(5)
    self.click_on_jw_library()