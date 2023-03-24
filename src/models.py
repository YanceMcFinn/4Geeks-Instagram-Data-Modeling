import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    username = Column(String(250), primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class User_isFollowing(Base):
    __tablename__= 'User_isFollowing'
    id = Column(String(250), primary_key=True)
    username_user = Column(String(250), ForeignKey('User.username'))
    username_followed = Column(String(250), ForeignKey('User.username')) 

class User_FollowedBy(Base):
    __tablename__= 'User_FollowedBy'
    id = Column(String(250), primary_key=True)
    username_user = Column(String(250), ForeignKey('User.username'))
    username_follower = Column(String(250), ForeignKey('User.username')) 

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), ForeignKey('User.username'))
    caption = Column(String(250), nullable=True)
    imagePath = Column(String(250), nullable=False)


class Post_Likes(Base):
    __tablename__ = 'Post Likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))
    username_likedby = Column(String(250, ForeignKey('User.username')))

class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), ForeignKey('User.username'))
    contents = Column(String(250), nullable=False)

class Comment_Likes(Base):
    __tablename__ = 'Comment Likes'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    username_likedby = Column(String(250, ForeignKey('User.username')))

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('user.username'))
#     person = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
