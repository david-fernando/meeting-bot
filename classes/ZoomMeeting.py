import time
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ZoomMeeting:

  def __init__(self):
    self.BRAVE_PATH = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    self.DRIVER_PATH = "Drive Path"
    self.ZOOM_METTING_URL = "Meeting URL"
    self.METTING_PASSWORD = "Password"
    self.options = webdriver.ChromeOptions()
    self.options.binary_location = self.BRAVE_PATH
    self.driver = webdriver.Chrome(executable_path=self.DRIVER_PATH, options=self.options)


  def open_zoom_metting_url(self):
    self.driver.get(self.ZOOM_METTING_URL)

  def open_zoom_metting_window(self):
    pyautogui.click(622, 236)
      

  def insert_metting_password(self):
    pyautogui.click(638, 320)
    pyautogui.write(self.METTING_PASSWORD)

  def click_on_join_the_meeting(self):
    pyautogui.click(627, 493)

  def enter_meeting(self):
    self.open_zoom_metting_url()
    time.sleep(40)
    self.open_zoom_metting_window()
    time.sleep(40)
    self.insert_metting_password()
    self.click_on_join_the_meeting()
