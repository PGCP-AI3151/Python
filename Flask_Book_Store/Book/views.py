from idlelib import redirector

from flask import render_template, redirect, url_for
from . import app
from .forms import RegistrationForm
from .models import Book


# books = [
#     {'title': 'Python Learning', 'author': 'abc', 'price': 10},
#     {'title': 'ML With Python', 'author': 'xyz', 'price': 50},
#     {'title': 'Java Learning', 'author': 'efg', 'price': 25},
# ]
@app.route('/')
def home():
    books = Book.query.all()
    # return '<h1>Hello World!</h1>'
    return render_template('home.html', books=books)


@app.route('/about')
def about():
    # return '<h2>About</h2>'
    return render_template('about.html', title='About Book Store')

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html', book=book)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('register.html', title='Register', form=form)