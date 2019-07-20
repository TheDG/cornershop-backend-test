# cornershop-backent-test
Technical test requires the design and implementation (using Django) of a basic management system to coordinate the meal delivery for Cornershop employees

##### Trello Board
* `https://trello.com/invite/b/Agr9GbdZ/47f7316d66653c7f0238493c294fef9a/cornershop-test`

##### Development setup (OSX Guide)

* Install brew
* Install pyenv
* Install pyenv-virtualenv
* Create Python 3.7 virtual environment and set it in .python-version file
* pip install -r stable-req.txt
* Setup PSQL DB
   * Create DB, User, Rol
* Setup env variables in .env inside cornershop project directory

#### Mount application
* `python manage.py runserver 3000`
* Open `localhost:3000` with any browser
