# Django example: Task form

This example shows:

- Usage of Django generic views
- Usage of Django generic forms
- Django with Bootstrap
- How to use pagination with generic views
- Default fixtures usage


## What does it do?

It will render a list of tasks. Some of them are provided as fixtures.

The list of tasks is provided as a Bootstrap table, and allows to add new tasks. If there are more than 5, they will be paginated.

You are allowed to create, edit or remove tasks.

## Usage

First of all, create the database. This will install the fixtures automatically:

    $ ./manage.py syncdb
    Creating tables ...
    Creating table django_admin_log
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_groups
    Creating table auth_user_user_permissions
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table todolist_task

    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): no
    Installing custom SQL ...
    Installing indexes ...
    Installed 42 object(s) from 1 fixture(s)

The user admin/admin will be created and some example tasks too.

Then run the server:

    $ ./manage.py runserver 7500
    Validating models...

    0 errors found
    January 06, 2014 - 11:12:25
    Django version 1.6.1, using settings 'example.settings'
    Starting development server at http://127.0.0.1:7500/
    Quit the server with CONTROL-C.

And it will be listening on localhost:7500


## To be done

- Render Date fields as dates.
- Add tests.