# coding=utf-8
"""
File: get_device_sn.py
Author: bot
Created: 2023/12/20
Description:
"""
import re
import subprocess
from typing import List


def get_device_sn() -> List[str]:
    result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE)
    devices = re.findall(r"\n" + "(.*)" + r"\tdevice", result.stdout.decode("utf-8"))
    return devices

