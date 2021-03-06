from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Login
from pages.login.login import login
app.register_blueprint(login)

## Logout
from pages.logout.logout import logout
app.register_blueprint(logout)

## Profile
from pages.profile.profile import profile
app.register_blueprint(profile)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)


###### APIs
## Users API
from apis.users.users_api import users_api
app.register_blueprint(users_api)
