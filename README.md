# Django Web Appliation Assignment

This directory of the repository contains the source code of web application which is based out on Django's Model-View-Controller (MVC) Architecture. 

### Various applcations
	- Authentication and authorization system
	- Automated confirmation email sending upon signup/registerd on the decision
	- Redis for Caching

### Development Setup for Django
Please follow the below guidelines to setup the development environment.

- Clone the repository: https://github.com/shbd845/Assignment.git
- Change the working directory to your cloned repository folder: `cd ../{your_repository_folder}`
- Installing the virtualenv package: `pip install virtualenv`
- Creating the virtual environment: `virtualenv env`
- Activating the environment: `env\Scripts\activate`
- Set up the `.env` file in the `/project1` folder.
	- The `.env` file should be created from the `.env.example` file [here]().
- Installing the required modules: `pip install -r requirements.txt`
- Making the migrations ready: `python manage.py makemigrations`
- Migrating the models to the DB: `python manage.py migrate`
- Running the server: `python manage.py runserver`
- Open your browser and navigate to `localhost:8000`