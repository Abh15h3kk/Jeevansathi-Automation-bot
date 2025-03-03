# Jeevansathi Automation Bot

## Overview
This project uses **Selenium** to log into the Jeevansathi website, process profiles, and send interest with custom messages based on specific filters you've applied to your partner preferences.  

The code is **modular**, with separate files for:  
- Configuration  
- Browser setup  
- Login  
- Profile processing  

### `.env` File Configuration  
Create a `.env` file in the root folder with the following credentials and preferences:

EMAIL=""

PASSWORD=""

MESSAGE=""

#Comma-separated list of occupations to exclude

EXCLUDED_OCCUPATIONS=Teacher,Professor,Lecturer,Others,Clerk

#Comma-separated list of occupation prefixes that are allowed (e.g., must start with)

ALLOWED_OCCUPATION_PREFIXES=Govt.,Civil Services

#Comma-separated list of keywords that are allowed anywhere in the occupation string

ALLOWED_OCCUPATION_KEYWORDS=Doctor,Surgeon,Army,Air,Defence


