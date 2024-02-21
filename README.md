# LAB - Class 31

## Project: Sneakers Project

- Author: Ekow Yawson

### Collaborators

- Stephanie Johnson
- Latherio Kidd

### Overview

In this iteration, we will rebuild a custom version of Things API demo project from scratch called Sneaker API.

### Links and Resources

- [What is Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
- [First Django App - Part 1](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- [First Django App - Part 2](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)

### Feature Tasks and Requirements

- [x] Update Dockerfile and docker-compose.yml if needed.

### Stretch Goals

- [ ] Research using a production server vs. the built in development server.
- [ ] Research using postgres instead of sqlite as database.

### Setup

#### How to initialize/run your application

To run this app, you must:

1. Create a Python virtual environment.
2. Enter the virtual environment.
3. Run `pip install -r requirements.txt`
4. Run the server with: `python manage.py runserver`
5. Follow the link provided in the CLI.

**Note**: This is a development build. Do not run it in Production.

### Tests

- [x] Test Model
  - String representation
  - All fields

To run the contained tests, issue the following command in the CLI:

```bash
python manage.py test
```
