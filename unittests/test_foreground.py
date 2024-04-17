import unittest
from colored.colored import Colored
from colored.library import Library
from colored.colored import fore, fore_rgb
from colored.foreground import Fore


class TestForeground(unittest.TestCase):

    def setUp(self):
        self.ESC: str = '\x1b['
        self.FOREGROUND_256: str = f'{self.ESC}38;5;'
        self.FOREGROUND_RGB: str = f'{self.ESC}38;2;'
        self.END: str = 'm'

    def test_foreground_256_code(self):
        for code in Library.COLORS.values():
            color = Colored(code)
            self.assertEqual(f'{self.FOREGROUND_256}{code}{self.END}', color.foreground())

    def test_foreground_256_name(self):
        for name, code in Library.COLORS.items():
            color = Colored(name)
            self.assertEqual(f'{self.FOREGROUND_256}{code}{self.END}', color.foreground())

    def test_fore_256_func(self):
        for name, code in Library.COLORS.items():
            color = Colored(name)
            self.assertEqual(fore(code), color.foreground())

    def test_foreground_rgb(self):
        for code in Library.COLORS.values():
            self.assertEqual(f'{self.FOREGROUND_RGB}{code};{code};{code}{self.END}', Fore.rgb(code, code, code))

    def test_foreground_rgb_func(self):
        for code in Library.COLORS.values():
            self.assertEqual(f'{self.FOREGROUND_RGB}{code};{code};{code}{self.END}', fore_rgb(code, code, code))


if __name__ == '__main__':
    unittest.main()
