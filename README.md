# LAB - Class 32

## Project: Sneakers Project

- Author: Ekow Yawson

### Collaborators

- Stephanie Johnson
- Latherio Kidd

### Overview

In this iteration, we will merge the functionalities of the previous project with this current one. We are customizing the project to use different application features/models than what was used in demos.

### Links and Resources

- [What is Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
- [First Django App - Part 1](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- [First Django App - Part 2](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)

### Feature Tasks and Requirements

- [x] Make your site a DRF powered API as you did in previous lab.
- [x] Adjust project’s permissions so that only authenticated user’s have access to API.
- [x] Add a custom permission so that only appropriate users can update or delete it.
- [x] Add ability to switch user’s directly from browsable API.

#### Feature: Docker

- [x] Create Dockerfile based off python:3.10-slim
- [x] Create docker-compose.yml to run Django app as a web service.
- [x] Enter docker compose up --build to start your site.
- [x] Add postgres as a service
- [x] Go to browsable api and confirm site properly restricts users based on their permissions.

### Stretch Goals

- [x] Research using a production server vs. the built in development server.
- [x] Research using postgres instead of sqlite as database.
- [ ] Try different permission levels, including custom ones.
- [x] Figure out how to directly access postgres running inside container. Hint: it will take research.
- [ ] Add a volume to persist data when container is shut down.

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
