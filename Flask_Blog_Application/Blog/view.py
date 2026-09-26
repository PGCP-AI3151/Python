from . import app
from flask import render_template

blog_posts = [
    {
        "title": "Getting Started with Flask 3.0",
        "content": "Flask remains one of the most popular micro-frameworks for Python. In this guide, we explore setting up your very first application factory pattern, structuring blueprints, and configuring environment variables for production environments.",
        "author": "Viraj"
    },
    {
        "title": "Mastering SQLAlchemy Relationships",
        "content": "Database relationships can be tricky for beginners. We break down the differences between one-to-many, many-to-many, and backrefs in Flask-SQLAlchemy so you can design clean schemas for complex blog platforms.",
        "author": "Vikram"
    },
    {
        "title": "How to Secure Flask Apps with WTForms",
        "content": "Cross-Site Request Forgery (CSRF) is a massive threat to modern web apps. Learn how Flask-WTF handles hidden security tokens automatically and validates complex backend forms gracefully using custom validators.",
        "author": "Viraj"
    },
    {
        "title": "Top 5 Python Layout Design Tips",
        "content": "Writing clean Python code involves adhering closely to PEP 8 standards. Beyond styling scripts, organizing your package structures with proper __init__.py tracking ensures clean code maintainability down the road.",
        "author": "Neha"
    },
    {
        "title": "Bootstrap 5 Utilities for Fast UI Dev",
        "content": "Stop writing endless custom CSS media queries. Bootstrap 5 layout grids, gap modifiers, flexboxes, and text utilities allow creators to engineer beautiful, fully responsive application interfaces in record time.",
        "author": "Vikram"
    },
    {
        "title": "Understanding Python's Virtual Environments",
        "content": "Isolating workspace dependencies prevents catastrophic environment conflicts. This deep-dive tutorial demonstrates how to leverage venv, pip freeze, and requirements configurations like a professional engineer.",
        "author": "Amit"
    },
    {
        "title": "Demystifying Flask Application Contexts",
        "content": "Ever run into an 'Error: Working off-context' runtime trace? We unpack exactly why Flask isolates application environments and how to use the 'with app.app_context()' wrapper safely in terminal scripts.",
        "author": "Viraj"
    },
    {
        "title": "Designing a Clean RESTful API",
        "content": "Web development relies heavily on reliable endpoints. Explore HTTP request methods like GET, POST, PUT, and DELETE, and see how Flask's native jsonify handles object serialization elegantly.",
        "author": "Rohan"
    },
    {
        "title": "Deploying Flask Apps to Production",
        "content": "Moving past local host environments requires a reliable WSGI server. Learn how to configure Gunicorn, reverse proxy configurations using Nginx, and manage secure application environments.",
        "author": "Vikram"
    },
    {
        "title": "Why Jinja2 is a Game-Changer",
        "content": "Template inheritance cuts code redundancy down dramatically. See how block overrides, dynamic loop variables, and localized filters breathe life into sterile HTML structures without rendering delays.",
        "author": "Priya"
    }
]


@app.route('/')
def home():
    return render_template('home.html',blog_posts = blog_posts)