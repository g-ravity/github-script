<p align="center">
    <img width="300" src="https://github.com/g-ravity/github-script/blob/master/github.png"/>
    <br>
    <img src="https://forthebadge.com/images/badges/made-with-python.svg"/>
    <img src="https://forthebadge.com/images/badges/powered-by-responsibility.svg"/>
</p>

# Github Script

A simple Python script to create, clone and delete repositories from the terminal.
Avoid the hassles of mouse, clicks and browser.
**Do it right from the terminal**

## Getting Started

- You need to have Chrome installed. Download it [here](https://www.google.com/intl/en_sg/chrome/)
- You need to have Python installed. Download it [here](https://www.python.org/downloads/)
- You need to install the Chrome Webdriver for your current version of Chrome
  - Check your current version of Chrome from Control Panel
  - Download ChromeDriver [here](http://chromedriver.chromium.org/downloads)
  - Save the .exe file, copy it's path, and add it to PATH in environment variables

## Usage

- Download/Clone the project
- Add your github credentials in the **info.json** file
- Run the script using the following command in terminal
  ```python
  python github.py
  ```
- Enter the name of repositories to be deleted, separated by a space

## Features To Be Added

- [ ] Creating a repository
- [ ] Cloning a repository
- [x] Deleting a repository

## How Does It Work?

- As soon as the script starts running, Chrome opens in headless mode
- Using the credentials in info.json file, you are logged into [Github](https://www.github.com/)
- The Selenium driver automatically navigates to your specified repos, and completes the necessary tasks
- A background thread runs in the terminal in the meanwhile, which shows a "waiting" animation

## Author

**Ravik Ganguly**

## License

This project is licensed under MIT License
