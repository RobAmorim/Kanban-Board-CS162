# CS162 Kanban Board 2:30 - Robson Silva

<br>
You can see the video showcase of the app in this link: 

## Project Structure

`static` css, images files, icons 
`templates` html files 
`app.py` main program 


## Virtual Environment and run the app
Creating virtualenv:

    $ virtualenv -p python3 venv

If doesn't work. Alternative:

    $ python3 -m venv venv

Now, activate the virtualenv. For Mac

    $ source venv/bin/activate

For **Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

Installing dependencies (virtual environment):

    $ pip3 install -r requirements.txt

Setting FLASK_APP varibales:

    $ export FLASK_APP=app

Stating the server:

	$ python3 -m flask run

Closing the virtual env.

    $ deactivate