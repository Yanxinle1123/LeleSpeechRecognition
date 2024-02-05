import os
import time

import langid
import speech_recognition as value_sr


def anim_print(value, delay=0.25, loop=1, final=' '):
    value_list = [x for x in value]  # 将输入的文本转换为字符列表
    i = 1
    while i <= loop:  # 循环指定的次数
        for char in value_list:
            print(f"\r{char}", end='', flush=True)  # 使用ANSI转义序列覆盖输出当前字符
            time.sleep(delay)  # 延时一段时间
        i += 1
    if final == ' ':
        print(f"\r{final}\b", end='', flush=True)  # 输出最终字符并退格
    else:
        print(f"\r{final}\n", end='', flush=True)  # 输出最终字符并换行


class Say:
    def __init__(self, text, rate=180):
        self.text = text
        self.rate = rate

    def say(self):
        os.system(f"say -r {self.rate} {self.text}")


class SR:
    def __init__(self, timeout=None, phrase_time_limit=None, language="zh-CN", print=True, computer_say=True,
                 anim=False):
        self.source = None
        self.timeout = timeout
        self.phrase_time_limit = phrase_time_limit
        self.language = language
        self.recognizer = value_sr.Recognizer()
        self.audio = None
        self.text = None
        self.print = print
        self.computer_say = computer_say
        self.anim = anim

    def sound_recording(self):
        try:
            with value_sr.Microphone() as self.source:
                if self.print:
                    print("正在调整噪音阈值, 预计需要2秒")
                if self.computer_say:
                    Say("正在调整噪音阈值, 预计需要2秒").say()
                self.recognizer.adjust_for_ambient_noise(self.source, duration=2.5)
                if self.anim:
                    anim_print(["噪音阈值调整中 ... 2", "噪音阈值调整中 ... 1", "噪音阈值调整中 ... 0"], 1)
                if self.print:
                    print("噪音阈值调整完毕")
                if self.computer_say:
                    Say("噪音阈值调整完毕").say()
                if self.print:
                    print("请说话")
                if self.computer_say:
                    Say("请说话").say()
                self.audio = self.recognizer.listen(self.source, phrase_time_limit=self.phrase_time_limit)
                if self.print:
                    print("录音完成")
                if self.computer_say:
                    Say("录音完成").say()
        except KeyboardInterrupt:
            if self.print:
                print("错误")
            if self.computer_say:
                Say("错误").say()

    def identify(self):
        try:
            if self.print:
                print("正在处理录音")
            if self.computer_say:
                Say("正在处理录音").say()
            if self.anim:
                anim_print(["处理录音中 ... /", "处理录音中 ... —", "处理录音中 ... \\", "处理录音中 ... |"], loop=5)
            self.text = self.recognizer.recognize_google(self.audio, language=self.language)
            detected_language = langid.classify(self.text)[0]
            self.text = self.recognizer.recognize_google(self.audio, language=detected_language)
            if self.print:
                print("正在识别语音")
            if self.computer_say:
                Say("正在识别语音").say()
            if self.anim:
                anim_print(
                    ["识别语音中 ... /", "识别语音中 ... —", "识别语音中 ... \\", "识别语音中 ... |"],
                    loop=5)
            if self.print:
                print(f"您说的是: {self.text}")
            if self.computer_say:
                Say(f"您说的是{self.text}").say()
            return self.text
        except value_sr.WaitTimeoutError:
            if self.print:
                print("没检测到语音")
            if self.computer_say:
                Say("没检测到语音").say()
        except value_sr.UnknownValueError:
            if self.print:
                print("无法识别音频")
            if self.computer_say:
                Say("无法识别音频").say()
        except KeyboardInterrupt:
            if self.print:
                print("已退出")
            if self.computer_say:
                Say("已退出").say()
        except ValueError:
            if self.print:
                print("错误")
            if self.computer_say:
                Say("错误").say()
