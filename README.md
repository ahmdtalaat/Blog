# Django Blog App

---

Full-featured Blog application using django with an authentication system, A user can create an account, login, logout and reset his password.
Every user has a profile page with a default profile picture and the user can update his username, email and his profile picture.
A user can Create, Update and Delete a post.

**Getting Started**

> Running the application on your machine:-

-   \$ cd ~/Desktop
-   \$ clone this repo to your pc "git clone https://github.com/ahmdtalaat/Flamingo.git"
-   \$ cd ~/Desktop/DjangoBlogApplication
-   \$ pip install pipenv
-   \$ pipenv install
-   \$ pipenv shell
-   \$ python3 manage.py runserver

> Running the application using docker containers, first you should have docker and docker-compose installed on your machine: https://tuleap-documentation.readthedocs.io/en/latest/developer-guide/quick-start/install-docker.html and then copy and paste the following commads:-

-   \$ cd ~/Desktop
-   \$ clone this repo to your pc "git clone https://github.com/ahmdtalaat/Flamingo.git"
-   \$ cd ~/Desktop/DjangoBlogApplication
-   \$ docker pull ahmdtalat95/django_app
-   \$ docker-compose up -d --build
