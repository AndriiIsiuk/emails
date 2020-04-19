# Mails sender

Basic mails sender service.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for _development_ and _testing_ purposes.

### Prerequisites

* Python >= 3.7 <br />
* Django >= 2.2 <br />
* PostgreSQL >= 10.0 <br />


### Environment:
Before you run the project you need to create a **.env** file.<br>
Example of the content of this file you can find in `.env.example` file attached in the repo.

### Installing
##### Makefile
For the biggest simplicity this project has Makefile attached. To see full list of available commands run `make help`.<br>

##### Containers
This project is fully Dockerized. You can have this project development version up and running by calling:<br>
```
make build-dev
make dev
```
You can find running application under **http://0.0.0.0:8001/api/core/emails/**

### Available API
**GET**
```
/api/core/emails/
```
Shows a list of created mails in database.<br>
Response status code: `200`<br>

**POST**
```
/api/core/emails/
```
Creates and (optionaly, depending on `status` key) sends mails to recipients.<br>

**required keys**:<br>
- `sender` - valid email address.<br>
- `recipients` - list of valid email addresses.<br>
- `title` - title for the mail, string.<br>
- `message` - a content of the mail, string.<br>

**optional keys**:<br>
 - `file__N`: any key with type File will be counted as a mail attachment.
 - `status`: string, 2 options: *PENDING* and *SENT*.<br>
 - `priority`: string, 2 options: *HIGH* and *LOW*.<br>

Response status code: `201`

**GET**
```
/api/core/emails/<pk>/
```
Shows details about selected mail by its **pk**.<br>
Response status code: `200`

**GET**
```
/api/core/emails/<pk>/status
```
Shows status of the selected mail by its **pk**.<br>
Response status code: `200`

**POST**
```
/api/core/emails/send-all-pending/
```
Sends all currently pending mails. Works with 2 queues. Priority mails are send in the separate priority queue.<br>

Response status code: `204`
### Fixtures
Project has couple of fixtures attached, just run:
```
make load-fixtures
```


### Mailhog
Application supports [Mailhog](https://github.com/mailhog/MailHog) for emails sending testing.<br>
You can find it under:<br>
```
http://0.0.0.0:8025/
```
Credentials:
```
login: user
password: emailservice
```

### Running tests
You can run tests using [pytest](https://docs.pytest.org/en/latest/) with command:
```
make test
```
To check the code coverage run:
```
make coverage
```

### And coding style tests

Test style adjustments accordingly to PEP8. All code formatted with `black` code formatter, which I used as a git `pre-commit hook`.


### Security tests

Project code is checked against the most popular vulnerabilities with [bandit](https://bandit.readthedocs.io/en/latest/) tool (as git `pre-commit hook`).


### HOWTO:
**Description:**<br />
Make a POST request to `http://0.0.0.0:8001/api/core/emails/` with body:
```json
{
    "sender": "readme@send.it",
    "recipients": ["one@one.com", "two@two.com", "three@three.com"],
    "title": "Testing mail from Readme",
    "message": "Hello, I am readme test content",
    "status": "SENT"
}
```
You will recieve response `201` with json containing data of saved mail. Now you can go to `http://0.0.0.0:8025/` and you will find that email sent ;)

If you have loaded fixtures - you can make *POST* request to `/api/core/emails/send-all-pending/` and you will see 4 mails more sent.

**Tip:**<br />
You can repeat the same action simply running:
```bash
make flush-db
make load-fixtures
```
### Attachments
Every key which will be marked as *File* in **POST** request to `http://0.0.0.0:8001/api/core/emails/` will be counted as the mail attachment.

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org/) - Framework for API building
* [pytest](https://docs.pytest.org/en/latest/) - Just for tests
* [black](https://github.com/psf/black) - Uncompromising Python code formatter
* [Docker](https://docs.docker.com/) - Containers
* [Mailhog](https://github.com/mailhog/MailHog) - Mails testing



## Author

* **Andrii Isiuk** - [LinkedIn](https://www.linkedin.com/in/andrii-isiuk/)
