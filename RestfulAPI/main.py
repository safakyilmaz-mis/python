import random
from random import choice
from flask import Flask, json, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql import text

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/random")
def random():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    random_cafe_select = {key: value for key,value in random_cafe.__dict__.items() if key != '_sa_instance_state'}
    return jsonify(random_cafe=random_cafe_select)


@app.route("/all")
def all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafes_list = [{column.name: getattr(cafe, column.name) for column in Cafe.__table__.columns} for cafe in all_cafes]
    return jsonify(All_cafes=cafes_list)

@app.route("/search")
def search():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    if result:
        return jsonify(Filtered_cafes = [{column.name: getattr(cafe, column.name) for column in Cafe.__table__.columns} for cafe in result])
    else:
        return jsonify(Error="No cafes found for the given location."),404

    
# HTTP POST - Create Record

@app.route("/add", methods=["GET","POST"])
def add():
    new_cafe = Cafe(name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),)

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(message="Cafe added successfully."), 201    

# HTTP PUT/PATCH - Update Record

from werkzeug.exceptions import HTTPException

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={f"success": f"Successfully update price for the cafe {cafe.name}."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

# HTTP DELETE - Delete Record

@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(message=f"Successfully deleted cafe {cafe.name}.")
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


if __name__ == '__main__':
    app.run(debug=True)
