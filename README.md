# newsfeed
##### create a personalized newsfeed portal.

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.


##### Setup
> Dependencies

- Python 3.8.5
- Django 3.2.9
- PSQL 13.2


```
git clone https://github.com/mbrsagor/newsfeed.git
cd newsfeed
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
```

Then create `.env` file and paste code from `example.env` file and add all validate information.
###### After that run the server in development or production environment

##### Run development server:
```bash
./ manage.py migrate
./ manage.py createsuperuser
./ manage.py runserver
```

> <b>N:B:</b> I think, most of all instructions are added here as well as postman collections.
