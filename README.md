<a href="https://dslackw.gitlab.io/colored"> 
<img src="https://gitlab.com/dslackw/colored/-/raw/site/docs/images/colored.png" title="colored"></a>

## About

Colored, it's a simple Python library for color and formatting in terminal.
Collection of color codes and names for 256 color terminal setups. 
Colored now supports RGB color mode. As "true color" graphic cards with 16 to <a href="https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit" target="_blank">24 bits</a> of color became common, 
applications began to support 24-bit colors. Terminal emulators supporting setting 24-bit foreground and background 
colors with escape sequences include Xterm, KDE's <a href="https://en.wikipedia.org/wiki/Konsole" target="_blank">Konsole</a>, and iTerm, as well as all libvte based terminals,
including <a href="https://en.wikipedia.org/wiki/GNOME_Terminal" target="_blank">GNOME Terminal</a>.

The colors work with most terminals and terminals emulators.
<a href="https://en.wikipedia.org/wiki/ANSI_escape_code" target="_blank">ANSI/VT100 escape sequences</a> can be used in every programming languages.

Colored is powerful and easy to use:

```python title="Python 3.9.17"
>>> from colored import Fore, Back, Style
>>>
>>> Fore.red
'\x1b[38;5;1m'
>>>
>>> Back.red
'\x1b[48;5;1m'
>>>
>>> Style.reset
'\x1b[0m'
>>> 
>>> Fore.rgb('100%', '50%', '30%')
'\x1b[38;2;255;130;79m'
>>>
>>> print(f'{Fore.white}{Back.green}Colored is Awesome!!!{Style.reset}')
```
!!! success
    <p> >>> <span style="background-color: green">
      <span style="color: white">Colored is Awesome!!!</span></span>
    </p>

## Installing

Open up a terminal and install colored with <a href="https://pip.pypa.io/en/stable/" target="_blank">pip</a> command:

```bash
$ pip install colored
```

Alternatively, you can grab the latest source code from <a href="https://gitlab.com/dslackw/colored" target="_blank">GitLab</a>:
```bash
$ git clone https://gitlab.com/dslackw/colored.git
$ cd colored
$ pip install .
```

## Usage

The [User Guide](https://dslackw.gitlab.io/colored/user_guide/user_guide/#user-guide) is the place to go to learn how to use the library. 

The [API Reference](https://dslackw.gitlab.io/colored/api/attributes/) documentation provides API-level documentation.

## License

colored is made available under the MIT License. For more details, see [here](https://dslackw.gitlab.io/colored/license/#mit-license).

## Contributing

!!! info
    We happily welcome [contributions](https://dslackw.gitlab.io/colored/contributors/)!

## Donate

Did you know that we developers love coffee? 

[<img src="https://gitlab.com/dslackw/colored/-/raw/site/docs/images/paypaldonate.png" alt="paypal" title="donate">](https://www.paypal.me/dslackw)