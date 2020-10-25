from markupsafe import Markup
from flask import Blueprint
from wtforms.fields import TextAreaField
import os


class MdeField(TextAreaField):
    """MdeField extends `wtforms.fields.TextAreaField
    <https://wtforms.readthedocs.io/en/stable/fields.html#wtforms.fields.TextAreaField>`_

    ``id`` defaults to  ``wmd-input``. Do NOT change this.
    You can change the other parameters in the
    `WTForms Field base class.
    <https://wtforms.readthedocs.io/en/stable/fields.html#the-field-base-class>`_

    """
    def __call__(self, id='wmd-input', **kwargs):
        button_bar = Markup('<div id="wmd-button-bar"></div>')
        return button_bar + super().__call__(id=id, **kwargs)


class Mde(object):
    """ Pagedown Editor Class.

    Usage Model

    ..  code-block:: python

       app = Flask(__name__)
       mde = Mde(app)

    or

    ..  code-block:: python

        mde = Mde()

        def create_app():
            app = Flask(__name__)
            mde.init_app(app)
            return app
    """
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def context_processor(self):
        return dict(mde=self)

    def init_app(self, app):
        app.context_processor(self.context_processor)
        self.static_url_path = app.static_url_path + '/flask_mde'
        flask_mde_blueprint = Blueprint(
            'flask_mde',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=self.static_url_path,
        )
        # Static files will be accessible from the following folders
        # /static/flask_mde/js, /static/flask_mde/css
        app.register_blueprint(flask_mde_blueprint)

    def editor(self, name=str(), default=str()):
        """ Loads the Pagedown editor (without preview).

        :param name: Name of the textaread field.
        :type name: str, optional
        :param default: Default value in the the textaread field.
        :type default: str, optional
        :return: Editor markup.
        :rtype: `markupsafe.Markup \
        <https://markupsafe.palletsprojects.com/en/1.1.x/escaping/#markupsafe.Markup>`_

        Example of usage in Jinja2

        ..  code-block:: html

            {{mde.editor(name='e1', default='# Heading')}}
        """
        return Markup(
            f"""
            <div id="wmd-button-bar"></div>
            <textarea id="wmd-input" name="{name}">{default}</textarea>
            """
        )

    @property
    def preview(self):
        """ Loads the preview panel.

        Accessible as ``{{mde.preview}}`` in Jinja2.

        """
        return Markup('<div id="wmd-preview"></div>')

    def editor_with_preview(self, **kwargs):
        """ Loads the Pagedown editor and preview.

        :param name: Name of the textaread field.
        :type name: str, optional
        :param default: Default value in the the textaread field.
        :type default: str, optional
        :return: Editor markup.
        :rtype: `markupsafe.Markup \
        <https://markupsafe.palletsprojects.com/en/1.1.x/escaping/#markupsafe.Markup>`_

        Example of usage in Jinja2

        ..  code-block:: html

            {{mde.editor_with_preview(name='e1', default='# Heading')}}

        This will give (almost) the same effect as using

        ..  code-block:: html

            {{mde.editor(name='e1', default='# Heading')}}
            {{mde.preview}}
        """
        return self.editor(**kwargs) + self.preview

    @property
    def js(self):
        """ Loads the Javascript files.

        Accessible as ``{{mde.js}}`` in Jinja2.
        """
        js_markup_text = str()
        js_folder_path = os.path.join(self.static_url_path, "js")
        js_files = [
            "prettify.js",
            "Markdown.Converter.js",
            "Markdown.Sanitizer.js",
            "Markdown.Editor.js",
            "Markdown.Extra.js",
            "mde.js"
        ]
        for file_name in js_files:
            url = os.path.join(js_folder_path, file_name)
            script = f'<script type="text/javascript" src="{url}"></script>'
            js_markup_text += script + os.linesep
        return Markup(js_markup_text)

    @property
    def css(self):
        """ Loads the css files.

        Accessible as ``{{mde.css}}`` in Jinja2.
        """
        css_markup_text = str()
        css_folder_path = os.path.join(self.static_url_path, "css")
        css_files = [
            "prettify.css",
            "mde.css"
        ]
        for file_name in css_files:
            url = os.path.join(css_folder_path, file_name)
            link = f'<link rel="stylesheet" type="text/css" href="{url}">'
            css_markup_text += link + os.linesep
        return Markup(css_markup_text)
