from flask import Flask

app = Flask(__name__)


@app.route('/restaurants')
def restaurants():
    return 'List of restaurants'


@app.route('/restaurants/add')
def restaurantAdd():
    return 'Add a new restaurant'

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
