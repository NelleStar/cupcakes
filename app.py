from flask import Flask, request, render_template, jsonify, flash, session
from models import db, connect_db, Cupcake
from forms import NewCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secretkey'

app.app_context().push()
connect_db(app)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    """shows home page"""
    form = NewCupcakeForm()

    if form.validate_on_submit():
        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image - form.image.data

        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(new_cupcake)
        db.session.commit()

    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes, form=form)

@app.route('/api/cupcakes')
def list_cupcakes():
    """Get all cupcakes from db and respond with them as json"""

    # uses list comprehension to serialize each cupcake in the cupcakes list
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """get info of one cupcake based on id"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """create new instance of a cupcake"""
    new_cupcake = Cupcake(flavor=request.json['flavor'],
                          size=request.json['size'],
                          rating=request.json['rating'])
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """update specifics about a cupcake but leave id alone"""

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")