# coding=utf-8
"""
File: img_shower.py
Author: bot
Created: 2023/12/20
Description:
"""
from typing import IO

from PIL import Image


def open_img_from_byte(stream: IO[bytes]) -> None:
    """
    Open the byte stream with Pillow as img
    :param stream:
    :return:
    """
    if stream is None:
        raise Exception("异常stream")
    image = Image.open(stream)
    image.show()

