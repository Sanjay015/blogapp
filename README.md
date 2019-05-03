Blogging Application
--------------------
- __About__
  - This blogging application is build on `django-2.1.2`
  - You can create, delete and edit blogs
  - All blogs will be available public
  - Only `author` of blog is authorized to `delete` or `edit` the blog
  - User need to first login to `create` a new blog
  - A user can create new account(`SignUp`) if not already have account
  - By default a list view of blog will be shown, by clicking on any block you will be able to read full blog
  - Data is being stored in `Sqlite3 DB`

- __Requirements__
  - `django-2.1.2` or above
  - `python 3.6` or above
  - `font-awesome-4.7.0`, `JQuery`, `bootstrap 4` (Both of there are available in repository, need not to download)
  - Web browser (example- `Chrome`, `Firefox`)

- __How to Use__
  - Clone this repository
  - Navigate to the cloned repository
  - Open command prompt and run below commands in same order
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    - `python manage.py runserver`
  - Open `http://127.0.0.1:8000` in your browser
  - _Enjoy!_ Now you are using the blogging application
 
