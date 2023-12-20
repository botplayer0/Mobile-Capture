# coding=utf-8
"""
File: android_capture.py
Author: bot
Created: 2023/12/20
Description: Use exec-out command to capture android devices screenshot and show in the PC.
"""
from __future__ import annotations

from typing import IO
import subprocess


from utils.get_device_sn import get_device_sn
from utils.img_shower import open_img_from_byte


def get_screenshot_stream(device_sn: str) -> IO[bytes] | None:
    img_stream = subprocess.Popen(["adb", "-s", device_sn, "exec-out", "screencap", "-p"], stdout=subprocess.PIPE)
    return img_stream.stdout


if __name__ == '__main__':
    device = get_device_sn()[0]
    stream = get_screenshot_stream(device)
    open_img_from_byte(stream)
