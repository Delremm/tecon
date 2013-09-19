.. TODO: Complete the README descriptions and "about" section.

Tecon Project
========================================

About
-----

Test constructor. Allow to create and pass various tests, for example academic tests.


Prerequisites
-------------

see in ./requirements/ folder


TODO
~~~~

Pictures for answers;
immidiate answer;
show answers with green color on right questions;
various result depends on correct number of answers;

create page has too many requests for categories

VIDEO on the main page
time limit to answer questions.

Installation
------------

To setup a local development environment::

    mkvirtualenv tecon
    pip install -r requirements.txt
    edit tecon/settings/project.py    # Enter your DB credentials
    cp tecon/settings/local.py.example tecon/settings/local.py  # To enable debugging

    ./manage.py syncdb --migrate
    ./manage.py runserver

Compiling CSS files
~~~~~~~~~~~~~~~~~~~

To compile LESS_ files::

    lessc frontend/static/frontend/less/styles.less > frontend/static/frontend/css/styles.css 


License
-------

Describe project license here.


.. Add links here:

.. _django-fluent: http://django-fluent.org/
.. _LiveReload: http://livereload.com/
.. _guard-livereload: https://github.com/guard/guard-livereload
