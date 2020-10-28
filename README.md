# PROJECT NAME
## Awwards

## AUTHOR
* AokoMercyline

## DESCRIPTION
This is an application that allow user to post a project he/she has created and get it reviewed by his or her peers or rated according to design,usability and content.

## BEHAVIOUR DRIVEN DEVELOPMENT

* User must sign in to be able to post projects and review projects for others users.
* User is able to post project.

## FEATURES

* Users need to Sign in to the application to post projects and review projects.

* Users can view different projects and their details.

* Users can post a project to be rated/viewed.

* Users can search for different projects.

* Users can view projects overall score.

* Users can view their profile page with all their published projects.

* Users can rate/review other users' projects.


## SETUP INSTALLATION

1.Clone or download and unzip the repository from github,https://github.com/AokoMercyline/Awwards.git

2.Activate virtual environment using python3.8 as default handler virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate

3.Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

4.Create the Database

* psql
* CREATE DATABASE instacopy;
5.Create .env file and paste paste the following filling where appropriate:
-SECRET_KEY = '<Secret_key>' 
-DBNAME = 'instacopy' -USER = ''
 -PASSWORD = '' 
 -DEBUG = True
6.  Run initial Migration 
    -python3 manage.py makemigrations instagram 
    -python3 manage.py migrate .Run the app 
    -python3 manage.py runserver 
    -Open terminal on localhost:8000

## TECHNOLOGIES USED
* Python 3.8
* Bootstrap
* css
* HTML
* Postgress

## SUPPORT and Contact

contact me aokomercyline34@gmail.com

## LICENSE
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2019.All rigths reserved
  
