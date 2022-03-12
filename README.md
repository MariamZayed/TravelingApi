# TravelingApi

# **Requirements**

- python 3.7.0
- latest pip version (in my case pip 22.0.3)
- latest Django version (in my case Django 3.2.12)

## Steps to clone the repo

1. **MUST** create a virtual environment for any OS
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

3. install django restframework for APIs and JWT Authentications<br>
    `pip install djangorestframework-simplejwt`<br>
    
4. install django-cors-headers <br>
   `pip install django-cors-headers`<br>
   CORS is a mechanism to allow interaction with resources hosted on different domains. In my case for example, React app <br>
   you can read more here: https://www.stackhawk.com/blog/django-cors-guide/

5. run migration to handle the models
   -  `python manage.py makemigration`
   -  `python manage.py migrate`

6. Finally, Run the server <br>
`python manage.py runserver`


## API Documentation 

<p>I'll put more detailed documention for APIs later, meanwhile, for instance you can route to the apis in next urls to:<br>
i. retrieve all data from the DB<br>
http://127.0.0.1:8000/api<br>
ii. retrieve single trip, using trip id as and endpoint<br>
http://127.0.0.1:8000/api/1 </p>

