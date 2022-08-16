from captcha.image import ImageCaptcha
import base64
from random import randint


class MyCaptcha:

    def __init__(self, width=200, height=100, char_count=4, text=None):
        self.width = width
        self.height = height
        self.char_count = char_count
        self.base_image = ImageCaptcha(width=self.width, height=self.height)
        self.captcha_text = None
        if not self.captcha_text:
            self.captcha_text = self.generate()
        else:
            self.captcha_text = text
        self.io_image = self.base_image.generate(self.captcha_text)
        self.html = base64.b64encode(self.io_image.getvalue()).decode()



    def generate(self):
        text = ''
        for i in range(0, self.char_count):
            char = randint(0, 15)
            text += f'{char:x}'

        return text

    def resolve(self, text):
        if str(text) == str(self.captcha_text):
            return True
        else:
            return False






