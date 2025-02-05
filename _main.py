import utime as time
time.sleep_us(10)
from usr.welcome_screen import WelcomeScreen
time.sleep_us(10)
from usr.main_screen import MainScreen
time.sleep_us(10)
from usr.setting1_screen import SettingScreen
time.sleep_us(10)
from usr.setting2_screen import Setting2Screen
time.sleep_us(10)
from usr.dev1_screen import Dev1Screen
time.sleep_us(10)
from usr.dev2_screen import Dev2Screen
time.sleep_us(10)
from usr.weather_screen import WeatherScreen
time.sleep_us(10)
from usr.about_screen import AboutScreen
time.sleep_us(10)
from usr.alarm_screen import AlarmScreen
time.sleep_us(10)
from usr.monitor_screen import MonitorScreen
from usr.Agri_ui import AgriUi


if __name__ == "__main__":
    print("main start...")

    agri_ui = AgriUi()
    agri_ui.add_screen(WelcomeScreen()) \
        .add_screen(MainScreen()) \
        .add_screen(MonitorScreen()) \
        .add_screen(SettingScreen()) \
        .add_screen(Setting2Screen()) \
        .add_screen(Dev1Screen()) \
        .add_screen(Dev2Screen()) \
        .add_screen(WeatherScreen()) \
        .add_screen(AboutScreen()) \
        .add_screen(AlarmScreen())

    print(agri_ui.screens)
    agri_ui.start()
