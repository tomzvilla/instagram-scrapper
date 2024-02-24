# imports for env variables 

import os
from dotenv import load_dotenv

load_dotenv()

class EnviromentVariable:
    def __init__(self):
        self.IG_USERNAME = os.getenv("IG_USERNAME")
        self.IG_PASSWORD = os.getenv("IG_PASSWORD")
        self.PROFILE_FOLLOWERS_URL = os.getenv("PROFILE_FOLLOWERS_URL")
        self.WAIT_TIME_IN_SECONDS = os.getenv("WAIT_TIME_IN_SECONDS")
        self.OLD_FOLLOWERS_FILENAME = os.getenv("OLD_FOLLOWERS_FILENAME")

        self.check_variables()

    def check_variables(self):
        missing_variables = []
        if not self.IG_USERNAME:
            missing_variables.append("IG_USERNAME")
        if not self.IG_PASSWORD:
            missing_variables.append("IG_PASSWORD")
        if not self.PROFILE_FOLLOWERS_URL:
            missing_variables.append("PROFILE_FOLLOWERS_URL")
        if not self.WAIT_TIME_IN_SECONDS:
            missing_variables.append("WAIT_TIME_IN_SECONDS")
        if missing_variables:
            raise ValueError(f"You need to specify the following enviroment variables: {', '.join(missing_variables)}")

envVars = EnviromentVariable()