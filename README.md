# cornershop-backend-test
Technical test requires the design and implementation (using Django) of a basic management system to coordinate the meal delivery for Cornershop employees

#### Trello Board
* `https://trello.com/invite/b/Agr9GbdZ/47f7316d66653c7f0238493c294fef9a/cornershop-test`

#### Staging app
* `https://obscure-bayou-88944.herokuapp.com`

#### App Directory Description
* Lunch_Poll is the admin site for resources
* Pages include the static and authentication pages
* Users is the app for the admin to manage users
* Staff is the app for the managment of employee actions (choose menus)

#### Development setup (OSX Guide)

* Install brew
* Install pyenv
* Install pyenv-virtualenv
* Create Python 3.7 virtual environment and set it in .python-version file
* pip install -r stable-req.txt
* Setup PSQL DB
   * Create DB, User, Rol
* Setup env variables in .env inside cornershop project directory
* Create Admin User
* TODO: Migrations

#### Run Seedfile

* `python manage.py seed --mode=refresh`

#### Run linters

* Run all linters: `python ci/linters.py`

#### Run Quality Control

* tests: `python manage.py test`
* Coverage:
  * `coverage run --source='.' manage.py test`
  * `coverage report --skip-covered --fail-under=100`
* Full quality control: `python ci/rake_quality.py`
* ##### need to add additional apps to run_pylint file in CI directory


#### Mount Dev application
* `python manage.py runserver 3000`
* Open `localhost:3000` with any browser

#### Additional Notes
* For the Employee automatic auth the flow is as follows.
  * URL is send with a his username encrypted and attached to the url
  * When employee clicks link encrypted-user is used decrypted with key stored in menu
  * Checks if user is present in DB
  * Logins in user
