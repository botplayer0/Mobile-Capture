# coding=utf-8
"""
File: ios_capture.py
Author: bot
Created: 2023/12/20
Description:
"""
import subprocess


def get_ios_screenshot():
    # brew install libimobiledevice
    process = subprocess.Popen(['idevicescreenshot', '-o', '/tmp/screenshot.png'])
    process.wait()
    with open('/tmp/screenshot.png', 'rb') as f:
        return f.read()