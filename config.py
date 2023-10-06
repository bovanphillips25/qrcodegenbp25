"""QR Code Generator Configuration"""
import os


class Config:
    IMAGE_DIRECTORY = os.environ.get('IMAGE_DIRECTORY', 'qrcodeimages')
    URL = os.environ.get('URL', 'https://github.com/bovanphillips25')
    FILE_NAME = os.environ.get('FILE_NAME', 'github.png')