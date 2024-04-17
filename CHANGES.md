COLORED
=======

Version 2.2.3 - *(07-07-2023)*
------------------------------
### Fixed
- Typing error #29

Version 2.2.2 - *(26-06-2023)*
------------------------------
### Added
- Set for environment variable $COLORTERM

### Updated
- Maximum number range for RGB colors

Version 2.2.1 - *(25-06-2023)*
------------------------------
### Updated
- Exception InvalidNavigation -> InvalidControl

Version 2.2.0 - *(24-06-2023)*
------------------------------
### Added
- CSI (Control Sequence Introducer) sequences
- SGR (Select Graphic Rendition) parameter style underline color
- Support RGB color schema

### Updated
- cprint() to support RGB colors

### Fixed
- Typo for style 'underlined', changed to 'underline'

Version 2.1.1 - *(20-06-2023)*
------------------------------
### Updated
- Legacy support versions 1.x.x: 
    * Functions fg(), bg(), attr() are back until deprecated to the future.
- Class attributes fore, back and style will be available also but instead imported them directly, you can use like the examples below:
    * from colored.foreground import fore 
    * from colored.background import back
    * from colored.attributes import style

Version 2.1.0 - *(20-06-2023)*
------------------------------
### Updated
- Updated library for default values
- Replace function show_colour() with cprint()

### Added 
- cprint(text, foreground='', background='', formatting='', reset=True, **kwargs) function

Version 2.0.0 - *(19-06-2023)*
------------------------------
### Updated
- Coding style
- For typing hints
- Class names:
    * fore -> Fore
    * back -> Back
    * style -> Style
- Function names:
    * fg() -> fore()
    * bg() -> back()
    * attr() -> style()
- Class attributes styles and colors in lower case, example:
    * Fore.red is the same Fore.RED
    * Style.bold is the same Style.BOLD
### Added
- Documentation site: https://dslackw.gitlab.io/colored
- Styles italic and strikeout #22
- Function show_colour()

Version 1.4.4 - *(09-11-2022)*
------------------------------
### Updated
- Code style
- Switch to f string
- Removed python2 support
- Use windows types instead of raw ctypes. Ref #25

Version 1.4.3 - *(23-10-2021)*
------------------------------
### Updated
- Improve color enabling #18

Version 1.4.2 - *(09-12-2019)*
------------------------------
### Updated
- Python 3 compatibility
- setup.py file 

Version 1.4.1 - *(28-10-2019)*
------------------------------
### Fixed
- UnsupportedOperation: fileno when detecting TTY #14

Version 1.4.0 - *(02-10-2019)*
------------------------------
### Added
- Ensure package data is included !7
- Converted old package spec files to new format !9
- Hex improvements !11
- Enable colors in Windows' terminal !12
- Added an option to make colored tty aware !13

Version 1.3.93 - *(06-07-2018)*
------------------------------
### Fixed
- Typo in MANIFEST file

Version 1.3.92 - *(02-07-2018)*
------------------------------
### Fixed
- Converted CHANGELOG, LICENCE and MANIFEST to a PyPi compatible Version and changed setup.py accordingly. Related to #12

Version 1.3.8 - *(26-06-2018)*
------------------------------
### Fixed
- pip install #12

Version 1.3.7 - *(26-06-2018)*
------------------------------
### Fixed
- License typo and pip install #12

Version 1.3.6 - *(24-06-2018)*
------------------------------
### Fixed
- Fix license in setup file

Version 1.3.5 - *(24-06-2018)*
------------------------------
### Updated 
- Switch to GitLab repository
- Switch to MIT licence

Version 1.3.4 - *(07-05-2017)*
------------------------------
### Added
- readline-safe stylize_interactive() #6

Version 1.3.4 - *(20-01-2017)*
------------------------------
### Fixed
- Color capitalization
### Updated
- Year license

Version 1.3.3 - *(19-11-2016)*
------------------------------
### Updated
- Updated to make HEX codes case-insensitive #2
### Added
-  Added a `stylize()` convenience method #3 

Version 1.3.2 - *(02-11-2016)*
-----------------------------
### Updated
- Merge back and fore colors names

Version 1.3.1 - *(20-09-2016)*
------------------------------
### Added
- Color RED_3B
### Fixed
- Python3 print tests compatibility.

Version 1.3.0 - *(20-09-2016)*
------------------------------
### Updated
- Switch libraries to vars() method.

Version 1.2.2 - *(18-05-2016)*
------------------------------
### Updated
- Files licence.
- Color name dark_sea_sreen_X in dark_sea_green_X.
- Thanks to Clifford Ireland for contributing.

Version 1.2.1 - *(06-06-2015)*
------------------------------
### Updated
- Fix Python3 install.
- Added license each file.

Version 1.2.0 - *(06-06-2015)*
------------------------------
### Updated 
- Restore KeyError message for catching exceptions.
- Fix foreground double key.
- Update modules import.
- Update tests.

Version 1.1.5 - *(25-02-2015)*
------------------------------
### Updated
- Fix pep8 style

Version 1.1.4 - *(01-08-2014)*
------------------------------
### Updated
-  Add egg-info directory

Version 1.1.3 - *(11-07-2014)*
------------------------------
### Updated
- Fix version, remove attr.py conflict with colored.py

Version 1.1.2 - *(11-07-2014)*
------------------------------
### Feature
- Added class fore, back, style

Version 1.1.1 - *(10-07-2014)*
------------------------------
### Feature
- Added HEX code colors
- Added test_2.py
- Added HEX list

Version 1.1.0 - *(09-07-2014)*
------------------------------
### Feature
- Added new test_2.py and colors_list.txt
### Updated
- Fix Python 3 support

Version 1.0.9 - *(09-07-2014)*
------------------------------
### Updated
- Remove numbers from dictionary
- Fix KeyError

Version 1.0.8 - *(08-07-2014)*
------------------------------
### Updated
- create alias fg(), bg(), attr()

Version 1.0.7 - *(08-07-2014)*
------------------------------
### Updated
- Include two dictionary in one

Version 1.0.6 - *(07-07-2014)*
------------------------------
### Updated
- Include 16 colors in 256 colors. Create class and attributes.

Version 1.0.5 - *(05-07-2014)*
------------------------------
### Feature
- Added test_3.py

Version 1.0.4 - *(04-07-2014)*
------------------------------
### Feature
- Added test_2.py

Version 1.0.3 - *(03-07-2014)*
------------------------------
### Updated
- Remove screenshots directory

Version 1.0.2 - *(02-07-2014)*
------------------------------
### Feature
- Added support 256 colors

Version 1.0.1 - *(02-07-2014)*
------------------------------
### Feature
- Added test

Version 1.0.0 - *(02-07-2014)*
------------------------------
### Announcement
Released version 1.0.0
