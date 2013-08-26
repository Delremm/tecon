.. TODO: Complete the README descriptions and "about" section.

Tecon Project
========================================

About
-----

Describe your project here.

Prerequisites
-------------

- Python >= 2.6
- pip
- virtualenv (virtualenvwrapper is recommended)

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

To compile SASS_ files::

    gem install compass bootstrap-sass oily_png guard-livereload guard-compass

    guard

To enable LiveReload_ of ``*.css`` files during development, install a browser plugin:

* Firefox (2.0.9 dev release): https://github.com/siasia/livereload-extensions/downloads
* Everyone else: http://help.livereload.com/kb/general-use/browser-extensions

And toggle the "LiveReload" button in the browser at the desired page.

License
-------

Describe project license here.


.. Add links here:

.. _Compass: http://compass-style.org/
.. _django-fluent: http://django-fluent.org/
.. _LiveReload: http://livereload.com/
.. _guard-livereload: https://github.com/guard/guard-livereload
.. _SASS: http://sass-lang.com/
