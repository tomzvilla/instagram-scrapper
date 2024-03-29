# Instagram Scrapper

A python script that allows you to scrap your followers and check who unfollowed you

## Instalation

You need to install the following dependencies:

* Selenium
* Chrome WebDriver Autoinstaller
* Python Dotenv

Here is the easiest way to do so:

#### Selenium
```
pip install selenium
```
#### Chrome WebDriver Autoinstaller
```
pip install chromedriver-autoinstaller
```
#### Python Dotenv
```
pip install python-dotenv
```

## Usage
### Variables
First, you need to set the enviroment variables

| Variable               | Type    | Description                                                     |
| ---------------------- | ------- | --------------------------------------------------------------- |
| IG_USERNAME            | String  | **Required**. Your instagram username                           |
| IG_PASSWORD            | String  | **Required**.Your instagram password                            |
| PROFILE_FOLLOWERS_URL  | String  | **Required**. Your instagram profile url ending with /followers |
| WAIT_TIME_IN_SECONDS   | Integer | **Required**. The ammount of time (in seconds) the script will keep scrolling through your followers. I recommend 0.35 seconds per follower |
| OLD_FOLLOWERS_FILENAME | String  | **Not required**. The filename with your followers, generated by the script (you need to write the file extension too) |

### Running the script

1. Install all dependencies
2. Input all enviroment variables on an .env file
3. Run the script with `python3 main.py`
4. The followers list will be generated at the root level of the directory
5. The file with the old followers's list must be at root level