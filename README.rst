Flask-MDE: Pagedown for Flask
=============================

Release v1.2.0 | `Example application <https://markdowneditor.pythonanywhere.com/>`_

.. image:: https://img.shields.io/pypi/v/flask_mde
    :target: https://pypi.org/project/flask_mde/
    
.. image:: https://img.shields.io/pypi/l/flask_mde
    :target: https://pypi.org/project/flask_mde/

.. image:: https://img.shields.io/pypi/pyversions/flask_mde
    :target: https://pypi.org/project/flask_mde/

.. image:: https://readthedocs.org/projects/flask-mde/badge/?version=latest
    :target: https://flask-mde.readthedocs.io/en/latest/?badge=latest
   
.. image:: https://pepy.tech/badge/flask-mde
    :target: https://pepy.tech/project/flask-mde

-------------------

`Pagedown <https://github.com/StackExchange/pagedown>`_ Editor with
`Google code-prettify <https://github.com/google/code-prettify>`_ for 
`Flask <https://palletsprojects.com/p/flask/>`_. 
`WTForms <https://wtforms.readthedocs.io/en/stable/index.html>`_ integration supported.
From v1.2.0 Flask-MDE supports `pagedown-extra <https://github.com/jmcmanus/pagedown-extra>`_.

Pagedown is a Markdown editor and previewer popularised by its use on 
StackOverflow. You can use the *Flask-MDE* extension 
to integrate the Pagedown editor into your Flask application.

Installation
############
Installing Flask-MDE is simple with `pip <https://pip.pypa.io/en/stable/>`_. To install Flask-MDE, 
run the command 

..  code-block:: text

    pip install Flask-MDE

in your terminal

Basic Usage
###########
Assuming the following folder structure:

..  code-block:: text

    .
    ├── app.py
    └── templates/
        └── index.html

**Files**

*app.py*

..  code-block:: python

    from flask import Flask, render_template
    from flask_mde import Mde

    app = Flask(__name__)
    mde = Mde(app)

    @app.route('/')
    def index():
        return render_template(
            "index.html"
        )


    if __name__ == "__main__":
        app.run()

*templates/index.html*

..  code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        {{mde.css}}
    </head>
    <body>
        {{mde.editor()}}
        {{mde.preview}}
        {{mde.js}}
    </body>
    </html>


`Read the user guide to check out all the features. <https://flask-mde.readthedocs.io/en/latest/user-guide.html>`_

Licenses that apply
===================

1. `Flask-MDE License (MIT) <https://github.com/bittobennichan/Flask-MDE/blob/master/LICENSE>`_
2. `Pagedown-Extra License <https://github.com/a100q100/pagedown-extra/blob/master/LICENSE.txt>`_
3. `Pagedown License <https://github.com/StackExchange/pagedown/blob/master/LICENSE.txt>`_
