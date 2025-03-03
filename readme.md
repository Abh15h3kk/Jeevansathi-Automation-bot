# Jeevansathi Automatation Bot

## Overview
This project uses Selenium to log into Jeevansathi website, process profiles, and send interest with your custom messages based on the specific filters you've applied on your partner preference. The code is modular and divided into separate files for configuration, browser setup, login, and profile processing.

You need to create a .env file in root folder, which will have your credentials and preference
EMAIL=""
PASSWORD=""
MESSAGE=""
# Comma-separated list of occupations to exclude
EXCLUDED_OCCUPATIONS=Teacher,Professor,Lecturer,Others,Clerk
# Comma-separated list of occupation prefixes that are allowed (e.g., must start with)
ALLOWED_OCCUPATION_PREFIXES=Govt.,Civil Services
# Comma-separated list of keywords that are allowed anywhere in the occupation string
ALLOWED_OCCUPATION_KEYWORDS=Doctor,Surgeon,Army,Air,Defence


