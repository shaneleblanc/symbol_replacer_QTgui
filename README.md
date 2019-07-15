# Symbol Replacer 

![Symbol Replacer UI screenshot](https://raw.githubusercontent.com/shaneleblanc/symbol_replacer_QTgui/master/screenshot.png)

A python script to rename files and folders, replacing a list of user provided characters with a single user provider character. The "Test" option will produce a log file without making any changes. The "Run" option will produce a log file and make changes.

## Getting Started

Frozen/executable applications for all platforms are coming soon. See the Installing section below to use it now. 

### Prerequisites

* Python 3
* PySide2

### Installing

1. Clone the repository to a folder.
2. Create a virtual environment using pipenv or virtualenv (optional):
    1. `# virtualenv venv`
    2. `# source venv/bin/activate`
3. Install PySide2: `# pip install PySide2`
4. Run the application: `# python3.6 main.py`
5. Fill out the textboxes in the UI window, and click Test or Run. 

warning: Be aware this script will rename files and folders on your file system. Ensure you have the directory set correctly. It is recommended to use the Test function before running. 


## Built With

* [Qt Creator](https://www.qt.io/qt-features-libraries-apis-tools-and-ide/) - IDE for Qt UI development
* [PySide2](https://pypi.org/project/PySide2/) - The official Python module from the Qt for Python project
* [Python](https://www.python.org/) -

## Contributing

Coming soon.

## Versioning

Currently 0.1 (first working release/MVP)
[SemVer](http://semver.org/) may be used for future versions.

## Authors

* **Shane LeBlanc** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Coming soon.
