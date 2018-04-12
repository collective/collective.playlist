Using the development buildout
------------------------------

Create a virtualenv in the package::

    $ virtualenv -p <path to Python 2.7.x> --clear .
    
or if your system python is still 2.7::
    
    $ virtualenv --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout::

    $ ./bin/buildout

Start Plone in foreground:

    $ ./bin/instance fg
