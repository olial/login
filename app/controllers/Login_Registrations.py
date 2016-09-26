"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Login_Registrations(Controller):
    def __init__(self, action):
        super(Login_Registrations, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Login_Registration')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html')


    def success(self):
        return self.load_view('success.html')

    def register(self):
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'password_confirmation': request.form['password_confirmation']
        }

        register_status = self.models['Login_Registration'].register_user(data)
        if register_status['status'] == True:
            session['id'] = register_status['user']['id']
            session['first_name'] = register_status['user']['first_name']
            print register_status
            return redirect('/success')

        else:
            for message in register_status['errors']:
                flash(message)
                return redirect('/')

    def login(self):
        data = {
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        # print data
        login_status = self.models['Login_Registration'].login_user(data)
        if login_status['status'] == True:
            session['id'] = login_status['user']['id']
            session['first_name'] = login_status['user']['first_name']
            print login_status
            return redirect('/success')


        else:
            return redirect('/')

    def logout(self):
        session.pop('name', None)
        session.pop('id', None)
        return redirect('/')
