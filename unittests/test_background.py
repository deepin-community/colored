import unittest
from colored.colored import Colored
from colored.library import Library
from colored.colored import back, back_rgb
from colored.background import Back


class TestBackground(unittest.TestCase):

    def setUp(self):
        self.ESC: str = '\x1b['
        self.BACKGROUND_256: str = f'{self.ESC}48;5;'
        self.BACKGROUND_RGB: str = f'{self.ESC}48;2;'
        self.END: str = 'm'

    def test_background_256_code(self):
        for code in Library.COLORS.values():
            color = Colored(code)
            self.assertEqual(f'{self.BACKGROUND_256}{code}{self.END}', color.background())

    def test_background_256_name(self):
        for name, code in Library.COLORS.items():
            color = Colored(name)
            self.assertEqual(f'{self.BACKGROUND_256}{code}{self.END}', color.background())

    def test_back_256_func(self):
        for name, code in Library.COLORS.items():
            color = Colored(name)
            self.assertEqual(back(code), color.background())

    def test_background_rgb(self):
        for code in Library.COLORS.values():
            self.assertEqual(f'{self.BACKGROUND_RGB}{code};{code};{code}{self.END}', Back.rgb(code, code, code))

    def test_background_rgb_func(self):
        for code in Library.COLORS.values():
            self.assertEqual(f'{self.BACKGROUND_RGB}{code};{code};{code}{self.END}', back_rgb(code, code, code))


if __name__ == '__main__':
    unittest.main()
