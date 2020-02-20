:satisfied:

# Awards



## Description

## Project screeen shot 
![App](/static/images/Screenshot.png)

## Project live site

This is the live .[ Click for the demo](https://awwwwards001.herokuapp.com/)
This is the github repo link . [ Click for the demo](https://github.com/SkimaniKings/Awards.git)


![alt text](projects/static/images/awwards.png)

## User stories

- The User can create an account.
- If the user already has an account they can log into their accounts.
- A user can view websites posted by other users.
- A user can update their profiles.
- A user can post their projects on the website to be viewed by others.


## Behavior Driven Development
                                
   Input: The user enter their credentials as propted
   Output: The user is redirected to the log in page.

   NB: If the user enters wrong credentials he/she is prompted to enter new credentials. eg if the username is already taken.

2. The user is redirected to the log in page
   Input: The User enters the credentials that they used to sign up.
   Output: If the Information is entered correctly the user is redirected to the home page.

   NB: The User must enter correct information to proceed to the home page else they will be propted to re-enter their credentials.

3. The User can Update their Profiles
   Once A user is logged in their profile pages are loaded and User can Edit their Profiles.
   Input: A user types in the new profiles that they want.
   Output: After they are done success message appears that tells them that their info has been succesfully updated..

4. The user can upload a Project
   Input: The user uploads any project from their machines
   Output: The uploaded project is displayed on the home page.
5. The projects posted contain livelinks that navigate to the the websites live links
    - A button is present on just below the project description to cater for this function 
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

Copyright &copy; 2020.All rigths reserved

MIT License

Copyright (c) 2020 skimanikings

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

#### By **Simon Kimani**&trade;
