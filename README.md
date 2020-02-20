:satisfied:

# Awards



## Description



## Project live site

This is the live .[ Click for the demo](https://awwwwards001.herokuapp.com/)

![Image](projects/static/img/award.png)

![alt text](projects/static/images/awwards.png)

## User stories

- The User can create an account.
- If the user already has an account they can log into their accounts.
- A user can view websites posted by other users.
- A user can update their profiles.
- A user can post their projects on the website to be viewed by others.


## Behavior Driven Development
                                

## Setup/Installation requirements

1.Clone or download and unzip the repository from github, `https://github.com/SkimaniKings/Awards.git`

2. Create a vIrtual environment `pipenv <environment_name`

Activate virtual environment using python3.6 `source venv/bin/activate`

3. Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
4. Create the Database

- psql
- CREATE DATABASE instacopy;

4. Create .env file and paste paste the following filling where appropriate:

-SECRET_KEY = '<Secret_key>'
-DBNAME = 'instacopy'
-USER = '<Username>'
-PASSWORD = '<password>'
-DEBUG = True

5. Run initial Migration
   -python3.6 manage.py makemigrations instagram
   -python3.6 manage.py migrate
6. Run the app
   -python3.6 manage.py runserver
   -Open terminal on localhost:8000

## Technologies Used

- PYTHON 3.6
- DJANGO FRAMEWORK
- BOOTSTRAP
- CSS
- POSTGRESS

## Support and contact details

Get in touch through - 0713813919 - kimanisimon856@gmail.com

### License

Copyright &copy; 2019.All rigths reserved

#### By **Simon Kimani**&trade;
