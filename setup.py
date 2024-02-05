from setuptools import setup, find_packages

setup(
    name="LeleSR",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition",
        "langid",
        "pyaudio",
    ],
    author="YanXinle",
    author_email="1020121123@qq.com",
    description="语音识别的简化库",
    url="https://github.com/Yanxinle1123/LeleSpeechRecognition",
)
