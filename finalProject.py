from flask import Flask
from flask import render_template, redirect, request

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


Session = sessionmaker()
eng = create_engine("sqlite:///db.sqlite")
Session.configure(bind=eng)
session = Session()

app = Flask(__name__)

Base = declarative_base()


class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    alt = Column(String)
    legend = Column(String)
    width = Column(Integer)
    height = Column(Integer)
    path = Column(String)
    gallery_id = Column(Integer, ForeignKey('gallery.id'))
    gallery = relationship("Gallery")


class Gallery(Base):
    __tablename__ = 'gallery'
    id = Column(Integer, primary_key=True)


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    gallery_id = Column(Integer, ForeignKey('gallery.id'))
    gallery = relationship("Gallery")


class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    gallery_id = Column(Integer, ForeignKey('gallery.id'))
    gallery = relationship("Gallery")


class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship("Restaurant")

Base.metadata.create_all(eng)

@app.route('/')
def front():
    return render_template('front.html')


@app.route('/restaurants/')
def restaurants():
    print(session.query(Restaurant))
    return render_template(
        'restaurants.html',
        restaurants = [r for r in session.query(Restaurant)]
        )

@app.route('/restaurants/add', methods=['POST', 'GET'])
def restaurantAdd():
    if (request.method == 'GET'):
        return render_template("restaurantAdd.html")
    if (request.method == 'POST'):
        #g = Gallery()
        #imgs = [Images( for i in request.form.get("images"):
        r = Restaurant(
            name=request.form.get('name'),
            description=request.form.get('description')
            )
        session.add(r)
        session.commit()
        return redirect('/restaurants/{}'.format(r.id))

@app.route('/restaurants/<int:restaurantID>')
def restaurant(restaurantID):
    return 'This is a particular restaurant'

@app.route('/restaurants/<int:restaurantID>/edit')
def restaurantEdit(restaurantID):
    return 'This is a particular restaurant being edited'

@app.route('/restaurants/<int:restaurantID>/delete')
def restaurantDelete(restaurantID):
    return 'This is a particular restaurant being deleted'

@app.route('/restaurants/<int:restaurantID>/menu-item/<int:menuItem>')
def menuItem(restaurantID, menuItem):
    return 'This is a particular restaurant menu item.'

@app.route('/restaurants/<int:restaurantID>/menu-item/<int:menuItem>/edit')
def menuItemEdit(restaurantID, menuItem):
    return 'This is a particular restaurant menu item being edited'

@app.route('/restaurants/<int:restaurantID>/menu-item/<int:menuItem>/delete')
def menuItemDelete(restaurantID, menuItem):
    return 'This is a particular restaurant menu item being deleted'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
