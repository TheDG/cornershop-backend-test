# cornershop-backend-test
Technical test requires the design and implementation (using Django) of a basic management system to coordinate the meal delivery for Cornershop employees

#### Trello Board
* Backlog where most features with there attached pull request can be found
* `https://trello.com/invite/b/Agr9GbdZ/47f7316d66653c7f0238493c294fef9a/cornershop-test`

#### Staging app
* `https://obscure-bayou-88944.herokuapp.com`
* Admin username: diegosinay
* Admin password: 123123
* Add yourself to Slack app through: `https://join.slack.com/t/cornershopbac-mpl1399/shared_invite/enQtNjkzOTc5MDM2MDk5LWYwMWY1MDQ5ZjZhYzU5OGE1MGI0ZTUwYTQ3MWVlNWEzZTcxODI4YTA2MzFlMjg3MzhkMmYwZWY5NWY2OTA1MDQ`

#### Slack app
* `cornershopbac-mpl1399.slack.com`

#### App Directory Description
* Lunch_Poll is the admin site for resources
* Pages include the static and authentication pages
* Users is the app for the admin to manage users
* Staff is the app for the managment of employee actions (choose menus)

#### Development setup (OSX Guide)

* Install brew
* Install pyenv
* Install pyenv-virtualenv
* Install Redis: brew install redis
* Create Python 3.7 virtual environment and set it in .python-version file
* pip install -r stable-req.txt
* Setup PSQL DB
   * Create DB, User, Rol
* Setup env variables in .env inside cornershop project directory
* Run Migrations
* Run Seedfile to create Admin
* Register Users to Slack app through: `https://join.slack.com/t/cornershopbac-mpl1399/shared_invite/enQtNjkzOTc5MDM2MDk5LWYwMWY1MDQ5ZjZhYzU5OGE1MGI0ZTUwYTQ3MWVlNWEzZTcxODI4YTA2MzFlMjg3MzhkMmYwZWY5NWY2OTA1MDQ`
* Run Mass User creation in 'Users/new' page
  * Correct way to make sure slack notifications are correctly sent

#### Env File content
* DB_NAME
* DB_USER
* DB_PASSWORD
* SECRET_KEY
* PASSWORD
* SLACK_API_TOKEN
* REDIS_URL

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
* Go to project root directory
* run in one terminal: `python manage.py runserver 3000`
* run in one terminal: `redis-server`
* run in one terminal: `celery -A cornershop worker -l info`

* Open `localhost:3000` with any browser

#### Additional Notes
* For the Employee automatic auth the flow is as follows.
  * URL is send with a his username encrypted and attached to the url
  * When employee clicks link encrypted-user is used decrypted with key stored in menu
  * Checks if user is present in DB
  * Logins in user
* The Username in the Django application has to match the Slack ID for the reminder / notification to be sent
* Admin username is diegosinay
* Admin password is 123123

#### Missing work
* Specification in the pending and icebox in the Trello Board
* Due to time constrains not everything could be done. This was due to the fact that it took a much longer time to get acquainted with the Django framework than planed. This left only 5 days to do work in the actual project.
  * Decision made was made to keep linting code for style guidelines, but delay testing to the end(if time remains), in hope of developing all the functionalities.
* To check specifics of missing work see Trello pending column 
