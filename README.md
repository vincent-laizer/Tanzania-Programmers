# Tanzania-Programmers

The Tanzania Programmer community website source

## Features / TODOS

- [ ] Simplified code sharing
- [ ] Tech jobs in Tanzania
- [ ] Programming chat room
- [x] Access to tech trends / A Tech Blog
- [ ] QNA forum

## Development

#### install requirements

```cmd
pip install -r requirements.txt
```

#### run the server

- For linux users
```cmd
python src/manage.py runserver
```

- For windows users
```cmd
python src\manage.py runserver
```

go to 127.0.0.1:8000 to view the site.


## More info for developers

apps in the project

- authapp
    - for authentications 
    ## TODOS
        - [x] Register users
        - [x] Activate user via email
        - [x] Login users
        - [x] Password Reset / Forgotten password
        - [x] Change password

- admin dashboard
    ## TODOS
        - Administrative tasks
            - [x] list all users 
- blog app
    ## TODOS
        - [x] create a blog
        - [x] blog comments
        - [x] comment replies


migration commands

python manage.py makemigrations && python manage.py migrate
#

> for Tanzania from Tanzania 

#
