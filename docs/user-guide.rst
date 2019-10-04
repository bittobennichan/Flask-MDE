.. _User Guide:

User Guide
==========

.. _Installation:

Installation
############
Installing Flask-MDE is simple with `pip <https://pip.pypa.io/en/stable/>`_. To install Flask-MDE, 
run the command 

..  code-block:: text

    $ pip install Flask-MDE

in your terminal.

Basic usage
###########
Flask-MDE can be used without wtforms integration. 

For one Flask application, create the :py:class:`Mde <flask_mde.models.Mde>` object by passing it the application.

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

This will allow us to access the object from the Jinja templates, without passing it as
an argument to *render_template*. 

Let's take a look at the various components that need to be included in the template

* The :py:meth:`editor method <flask_mde.models.Mde.editor>` of the object will render the Pagedown editor in the template. 

* The :py:attr:`css property <flask_mde.models.Mde.css>` will include the css files.

* The :py:attr:`js property  <flask_mde.models.Mde.js>` will include the js files.

* The :py:attr:`preview property  <flask_mde.models.Mde.preview>` will render the preview panel.

*index.html*

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

Optionally a name and default value can be passed to the editor:

..  code-block:: html

    {{mde.editor(name='e1', default='# Heading')}}

Another method editor_with_preview will render the editor and preview panel in one go. 
This is less flexible if you want finer control over the appearence of editor and preview.

..  code-block:: html

    {{mde.editor_with_preview(name='e1', default='# Heading')}}

If you are using an application factory, the following pattern is also supported.

..  code-block:: python

    mde = Mde()

    def create_app():
        app = Flask(__name__)
        mde.init_app(app)
        return app

WTForms integration
###################

For WTForms compatibilty, use the :py:class:`MdeField<flask_mde.models.MdeField>` class. MdeField extends 
`wtforms.fields.TextAreaField
<https://wtforms.readthedocs.io/en/stable/fields.html#wtforms.fields.TextAreaField>`_.
MdeField can be customized via the Field definition. 
See: `WTForms - Field definitions 
<https://wtforms.readthedocs.io/en/stable/fields.html#field-definitions>`_.

You must NOT however change the ``id`` of the field. This is used by the css and js files.

**A Minimal example**

*app.py*

..  code-block:: python

    from flask import Flask, render_template
    from flask_mde import Mde, MdeField
    from flask_wtf import FlaskForm
    from wtforms import SubmitField

    app = Flask(__name__)
    mde = Mde(app)
    app.config['SECRET_KEY'] = "your_secret_key_here"

    class MdeForm(FlaskForm):
        editor = MdeField()
        submit = SubmitField()


    @app.route('/')
    def index():
        form = MdeForm()
        return render_template(
            "index.html",
            form=form
        )

*index.html*

..  code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        {{mde.css}}
    </head>
    <body>
        <form method="POST">
            {{form.csrf_token }}
            {{form.editor}}
            {{form.submit}}
        </form>
        {{mde.preview}}
        {{mde.js}}
    </body>
    </html>

Note that ``form.editor`` does not take any arguments. 
All the arguments need to be passed during field definition.

Converting to HTML
##################

Submitted text will be markdown. If you need to convert to HTML, 
you can use the `markdown <https://pypi.org/project/Markdown/>`_ library. 

Sanitizing HTML
###############
HTML sanitization can be used to protect against cross-site scripting (XSS) attacks 
by sanitizing any HTML code submitted by a user.
Once you have converted markdown to HTML, it is a good idea to sanitize the HTML
before displaying it on your site.

`Bleach <https://pypi.org/project/bleach/>`_ library can be used for this.

Making HTML pretty
##################
When you convert the markdown to HTML and displayit back on your application, 
it won't be similar to the preview shown. This is because `Google code-prettify <https://github.com/google/code-prettify>`_'s 
``prettyPrint`` function is not called.

Flask-MDE provides the ``make-pretty`` css class to make your HTML similar to that shown in the preview.

..  code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        {{mde.css}}
    </head>
    <body>
        <div class="make-pretty">
            {{output_html|safe}}
        </div>
        {{mde.js}}
    </body>
    </html>
