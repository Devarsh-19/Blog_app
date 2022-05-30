# Blog_application_django
A Blog application developed using Django framework 4.0.4

### Features:
- User Authentication - Users can register, login and logout
- Create, Edit and Delete Posts
- Users can Like and Comment on posts.
- Connections - Follow/Unfollow other users.

### Steps to be followed for first time use
- #### Set these Environment variables along with AWS Credentials

```
DEBUG_VALUE = True
DJANGO_ENV = DEV
SECRET_KEY_BLOG = <Your Secret Key>
```
- #### Run these commands - This will create your application tables (by the Model definition) in the Database.
```
python manage.py makemigrations

python manage.py migrate
```
- #### Create an ```admin``` user by running these following commands
```
python manage.py createsuperuser
```
- #### Run Tests to ensure everything is set up and working correctly.
```
python manage.py test
```
#### This will be updated regularly....