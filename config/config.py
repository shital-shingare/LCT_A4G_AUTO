import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
DASHBOARD_URL = os.getenv("DASHBOARD_URL", "http://lct-a4g-qa.accoladeelectronics.com/device-dashboard-page")
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
VIDEO_RECORDING = os.getenv("VIDEO_RECORDING", "false").lower() == "true"
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")
BASE_URL = os.getenv("BASE_URL")

# ❌ Invalid Credentials (for testing)
INVALID_USERNAME = os.getenv("INVALID_USERNAME", "ABC")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "12345")


# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PASSWORD")
