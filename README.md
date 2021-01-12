# django-datatables-view-sample

[django-datatables-view](https://pypi.org/project/django-datatables-view/)This is a sample application that you can actually move and try.

![Alt text](doc/nba_player_sample.png?raw=true "NBA Player Sample")

# How to use

１．Install python (3.5 or above) in advance.

２．Download the project with git

```
git clone https://github.com/okoppe8/django-datatables-view-sample.git
```

※ If you don't have git, you can also use "Clone or Download" → "Download ZIP" on the upper left.

３．Execute the setup command from the terminal

windows

```
cd django-datatables-view-sample
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
```

MacOS/Linux

```
cd django-datatables-view-sample
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

４．Launch the development service and open the URL from your browser

windows

```
manage.py runserver
```

MacOS/Linux

```
python manage.py runserver
```

URL

```
http://localhost:8000
```
