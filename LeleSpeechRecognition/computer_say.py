import os


class Say:
    def __init__(self, text, rate=180):
        self.text = text
        self.rate = rate

    def say(self):
        os.system(f"say -r {self.rate} {self.text}")


say = Say("你好, 我是你的电脑", 180)
say.say()
