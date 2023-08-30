from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange

class NewCupcakeForm(FlaskForm):
    """form for adding new cupcake"""

    flavor = StringField("Cupcake Flavor",
                         validators=[InputRequired(message="Flavor cannot be blank")])
    size = StringField("Size",
                       validators=[InputRequired(message="Must include size")])
    rating = FloatField("Rating", 
                        validators=[InputRequired(message="Please rate")])
    image = StringField("Photo URL")