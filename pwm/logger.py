from pwm.utils import KeyUtil
from pwm.window_manager import WindowManager
from pwm.bar import Bar
from pwm.action import Action
from pwm.Globals import TEST_GLobal


class Logger:
    def __init__(self):
        return


    def Testing():
        KeyUtil.sayHello()
        WindowManager.Test()
        Bar.Test()
        Action.tester()
        print(TEST_GLobal)
