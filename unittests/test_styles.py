import unittest
from colored.colored import Colored
from colored.attributes import Style
from colored.library import Library


class TestStyles(unittest.TestCase):

    def setUp(self):
        self.ESC: str = '\x1b['
        self.END: str = 'm'
        self.UNDERLINE_COLOR: str = f'{self.ESC}4;58;5;'

    def test_style_code(self):
        for code in Library.STYLES.values():
            style = Colored(code)
            self.assertEqual(f'{self.ESC}{code}{self.END}', style.attribute())

    def test_style_name(self):
        for name, code in Library.STYLES.items():
            style = Colored(name)
            self.assertEqual(f'{self.ESC}{code}{self.END}', style.attribute())

    def test_underline_color(self):
        for code in Library.COLORS.values():
            self.assertEqual(f'{self.UNDERLINE_COLOR}{code}{self.END}', Style.underline_color(color=code))


if __name__ == '__main__':
    unittest.main()
