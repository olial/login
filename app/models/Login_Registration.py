""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""

from flask import Flask, session, flash, Markup
import re
app = Flask(__name__)
app.secret_key = "SECRET"

from system.core.model import Model

class Login_Registration(Model):
    def __init__(self):
        super(Login_Registration, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """

    def register_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        errors = []

        # first_name = info['first_name']
        # last_name =  info['last_name']
        # email = info['email']
        # password = info['password']
        if not info['first_name']:
            errors.append("First name cannot be blank!")
            print ("First name cannot be blank!")

        elif len(info['first_name']) < 2:
            errors.append("First name must be letters only and have at least 2 characters!")
            print ("First name must be letters only and have at least 2 characters!")

        elif not NAME_REGEX.match(info['first_name']):
            errors.append("First name must be letters only!")
        

        elif len(info['last_name']) < 2:
            errors.append("Last name must have at least 2 characters!")
        

        elif not NAME_REGEX.match(info['last_name']):
            errors.append("Last name must be letters only!")
            

        elif len(info['email']) < 1:
            errors.append("Please enter a valid email!")
            
       
        elif not EMAIL_REGEX.match(info['email']):
            errors.append("Please enter a valid email!")
               

        elif len(info['password']) < 8:
            errors.append("Password must be at least 8 characters long!")
        

        elif (info['password'] != info['password_confirmation']):
            errors.append("Password and Password Confirmation must match!")
        
        if errors:
            return {"status": False, "errors": errors}
            flash(errors)

        else:
            # first_name = info['first_name']
            # last_name =  info['last_name']
            # email = info['email']
            password = info['password']
            pw_hash = self.bcrypt.generate_password_hash(password)
            query = "INSERT into users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
            data = {
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'email': info['email'],
                'pw_hash': pw_hash
            }
            self.db.query_db(query, data)

            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }
            # session['first_name'] = info['first_name']

    def login_user(self, info):
        password = info['password']
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {
            'email': info['email']
            }
        user = self.db.query_db(query, data)
        if user:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                # session['first_name'] = user[0]['first_name']
                # print session['first_name']
                return { "status": True, "user": user[0] }
    
        return {"status": False }
