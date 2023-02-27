from pwm.Config import Config
from pwm.Virt import Virt
from pwm.utils import KeyUtil
from pwm.window_manager import WindowManager
from pwm.bar import Bar
from pwm.action import Action
from pwm.Globals import (TEST_GLobal, NEXT_WINDOW, PREVIOUS_WINDOW )


class Logger:
    def __init__(self):
        return


    def Testing(self):
        KeyUtil.sayHello()
        WindowManager.Test()
        Bar.Test()
        Action.tester()
        print(TEST_GLobal)
        print(NEXT_WINDOW)
        print(PREVIOUS_WINDOW)
        Config.Test()
        Virt.Test()

    def ModifyConfig(self,Version, System, WindowSytem):
        config = Config("0.1", "Arch", "1920x1080")
        config.setVersion(Version)
        config.setSystem(System)
        config.setWindowSize(WindowSytem)

    def TestGlobals(self):
        print("test global: " , TEST_GLobal)
        print("Next window: ", NEXT_WINDOW)
        print("Previous Window: ", PREVIOUS_WINDOW)

logger = Logger() 
logger.TestGlobals()
logger.Testing()
logger.ModifyConfig("0.2", "Ubuntu", "1024x768")



