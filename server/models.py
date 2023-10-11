from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 
    @validates("name", "phone_number")
    def validate_author(self, key, value):
        if key == "name":
            if value is not None and len(value) >= 1:
                return value
            else:
                raise ValueError("Author must have a name")
            
        elif key == "phone_number":
            if len(value) == 10:
                return value
            else:
                raise ValueError("Phone numbers must be 10 digits long")

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 
    @validates("title", "content", "summary", "category")
    def validate_post(self, key, value):
        if key == "title":
            clickbait_keywords = [
                "Won't Believe",
                "Secret",
                "Top",
                "Guess",
                "Love"
            ]

            for keyword in clickbait_keywords:
                if keyword.lower() in value.lower():
                    raise ValueError("Warning: This post could be clickbait, please change it")
                
            if value is not None and len(value) >= 1:
                return value
            else:
                raise ValueError("Post must have a title")
            
        elif key == "content":
            if len(value) >= 250:
                return value
            else:
                raise ValueError("Post content must be at least 250 characters long")
            
        elif key == "summary":
            if len(value) < 250:
                return value
            else:
                raise ValueError("Post summary must be 250 characters or less")
            
        elif key == "category":
            if value == "Fiction" or value == "Non-Fiction":
                return value
            else:
                raise ValueError("Category must be Fiction or Non-Fiction")

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
