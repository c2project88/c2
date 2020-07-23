# C2 Project

## Installation

```bash
git clone https://github.com/c2project88/c2.git
pip install -r requirements/local
python manage.py migrate
python manage.py createsuperuser
python manage.py run server

go to http://127.0.0.1:8000
```

## for auth with google

access your admin page after login  
on the site section, click "sites"  
and fill

- Domain name:127.0.0.1:8000
- Display name:127.0.1:8000

back to admin homepage, under "Social Accounts" section click
"Social aplications" and fill out these settings:

- Provider:Google
- Name: Google Api
- cliend id: cliend id from your google developers project credentials
- secret key: cliend secret from your google developers project credentials
- sites: 127.0.0.1:8000

for more information abouth aunt read allaouth doc's
[link](https://django-allauth.readthedocs.io/en/latest/index.html)

Google Apis console
[link](https://console.developers.google.com/)
