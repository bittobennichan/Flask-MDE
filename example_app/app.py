from flask import Flask, render_template, request, flash, session
from flask_mde import Mde, MdeField
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import InputRequired, Length
import markdown
import bleach
import os

app = Flask(__name__)
# Create the Mde object
# https://flask-mde.readthedocs.io/en/latest/user-guide.html#basic-usage
mde = Mde(app)

# Don't do this in your production app
# https://stackoverflow.com/questions/27287391/
# Read your secret key from a config file or env variable
app.config['SECRET_KEY'] = os.urandom(24)


def error_flasher(form):
    """Flashes all error encountered while processing the form."""
    for field, message_list in form.errors.items():
        for message in message_list:
            flash(form[field].label.text + ': ' + message, 'error')


class MdeForm(FlaskForm):
    """ The editor form.

    Includesthe MDEField editor and submit button.
    """
    editor = MdeField(
        validators=[
            InputRequired("Input required"),
            Length(min=15, max=30000)
        ]
    )
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MdeForm()
    if form.validate_on_submit():
        # Save to session
        session['editor'] = request.form['editor']
        # Convert markdown to html
        html = markdown.markdown(request.form['editor'])
        # Tags deemed safe
        allowed_tags = [
            'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'img',
            'h1', 'h2', 'h3', 'p', 'br'
        ]
        # Attributes deemed safe
        allowed_attrs = {
            '*': ['class'],
            'a': ['href', 'rel'],
            'img': ['src', 'alt']
        }
        # Sanitize the html using bleach &
        # Convert text links to actual links
        html_sanitized = bleach.clean(
            bleach.linkify(html),
            tags=allowed_tags,
            attributes=allowed_attrs
        )
        return render_template('view.html', code=html_sanitized)
    else:
        error_flasher(form)
    # setting default value
    form.editor.data = session.get('editor', '')
    # Reaches here if not a valid POST request
    return render_template(
        "index.html",
        form=form
    )


if __name__ == "__main__":
    app.run()
