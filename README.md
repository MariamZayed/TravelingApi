# TravelingApi

# requirements

- python 3.7.0
- latest pip version (in my case pip 22.0.3)
- latest Django version (in my case Django 3.2.12)

## steps to clone the repo

1. **MUST** create a virtual environment, for any different OS
- for Windows users, after making sure of having python and pip installed, do the following
   - a. open the cmd and install virtualenv package
`pip install virtualenv`
   - b. after installing the package, go to dir you want your project to be in and create the virtual environment by this command
`virtualenv env_name` <br><br>
You shall find these folders (Scripts, Lib) and (pyvenv.cfg) file <br>
![Untitled](https://user-images.githubusercontent.com/66179261/156905473-240306db-abde-4c86-a4de-cbb02c07fcbe.jpg)
   - c. **MUST** activate the Virtual env to work properly. <br>
   Go to the the Virtual env and Activate it by pasting in cmd `Scripts\activate`

2. After creating virtual env, install Django 
`py -m pip install Django`

3. Run the server
`python manage.py runserver`
