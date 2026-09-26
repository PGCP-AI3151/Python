from . import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writer = db.Column(db.String(100),nullable=False)
    heading = db.Column(db.String(100),nullable=False)
    content = db.Column(db.String(150),nullable=False)

    def __repr__(self):
        return f'{self.heading}'
