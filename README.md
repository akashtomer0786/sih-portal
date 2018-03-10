# Portal Documentation

Django web app

### Structure:

```
Portal (Project)
├── portal (Project folder)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── introapp (App)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── templates
│       └── home.html
│
├── Analytics (App)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── templates
│       └── analytics_home.html
│
│
│
.
.   Login, and more will come
.
│
├── static (frontend related files)
│   ├── img
│   ├── css
│   └── js
├── README.md
├── requirements.txt
├── .env
└── manage.py
```

### Installation:

To install all dependencies, first change your path to root directory where manage.py file is there and type:

`pip install -r requirements.txt`

This will install everything required for this project.

*IMPORTANT:* Make sure you have activated your virtual environment first before installing all the dependencies.

### Frontend:

After seeing the structure you will notice that each app have it's own templates folder. So inside these templates folder
only you will be working. All the static files which are img, js, css files needs to be stored in static folder which can
be found in root folder.

### Database configuration:

Installation may vary for Ubuntu/Windows so take help of the internet.

Install Postgresql in your local machine and then later you will be able to access it by 'psql' in command line.
In case of error try to search it and find answer.

After using `psql` in command line, it should look something like this:

```
psql (9.5.11)
Type "help" for help.

postgres=#
```

Now here we will type and create our first user with password.

`CREATE ROLE sih WITH LOGIN PASSWORD 'password';`

Explanation:

`CREATE ROLE <USER> WITH LOGIN PASSWORD <PASSWORD>`

Now create one database which will be use by Django to store data

`create database sih_data;`

Explanation:

`CREATE DATABASE <DATABASE_NAME>`

Now we will provide all the privileges for the user so that django can use it and create tables in that database.

`GRANT ALL PRIVILEGES ON DATABASE sih_data TO sih;`

Explanation:

`GRANT ALL PRIVILEGES ON DATABASE <DATABASE_NAME> TO <USER>`

Now after typing this you will create one postgres url which will be used by django to access/modify/delete/create table from database.

DATABASE_URL: `postgresql://sih:password@localhost/sih_data`

Explanation: `postfresql://<user>:<password>@localhost/<database_name>`

*IMPORTANT*: After creating database the tables which will be created by Django will not be modified by you until and unless you know what you are doing.

### Getting Started

Go to root folder where manage.py folder is present and create one new file with name:
`.env`

This `.env` file will have all the credentials. If it is already present then edit the DATABASE_URL with your database url which you created from above steps. These details must be confidential and need not to be exposed on the internet.

After setting up the virtual environment, installing all the dependencies and setting up the database you are ready to start
your server.

Step 1: Go to root folder of this repository and run
`python manage.py runserver`

*Note*: Make sure you are using Python is 3.6 or 3.5 version.

Step 2: If that works fine, then you are ready to set up the tables. Now type:
`python manage.py makemigrations` (Not important but this command checks if you need any migration or not)

`python manage.py migrate`

Step 3: Now you must see OK after every table executed. If this works fine then you are ready. Now you can start developing.
