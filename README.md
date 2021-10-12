# BUILD A PHOTO FEED USING DJANGO

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

- Clone this repository by running: 
```
git clone https://github.com/YAELMOR/Crime-Detection.git
```
- Change directory to the cloned repo
```
cd pusher_django_photo_feed
```
- Install required libraries: i.e pusher and django
```
pip install django pusher
```

#### Database Migrations
 - Run the following command at the root of your application to  make the migrations needed for the database
 
 ```
 python manage.py makemigrations
 ```
 
 - Run this command to migrate the database
 
 ```
  python manage.py migrate
 ```

And finally, start the application:

```
python manage.py runserver.
```
and visit http://localhost:8000/ to see the application in action.
## Built With

* [Pusher](https://pusher.com/) - APIs to enable devs building realtime features
* [DJango](https://docs.djangoproject.com/) - The web framework for perfectionists with deadlines. 
* [Jquery](https://jquery.com/) - The Write Less, Do More, JavaScript Library

