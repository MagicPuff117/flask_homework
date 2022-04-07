from flask import Flask, jsonify, request
from flask.views import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from jsonschema import validate, ValidationError
import datetime as dt




PG_DSN = 'sqlite:///hw.db'
app = Flask('hw_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=PG_DSN, SQLALCHEMY_TRACK_MODIFICATIONS=False)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AdModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(128), index=True)
    description = db.Column(db.String(300), index=True)
    date = db.Column(db.DateTime, default=dt.datetime.now())



class AdView(MethodView):

    def get(self, ad_id):
        ad = AdModel.query.get(int(ad_id))
        return jsonify({
            'header': ad.header,
            'description': ad.description,
            'date': ad.date
        })




    def post(self):

        new_ad = AdModel(**request.json)
        db.session.add(new_ad)
        db.session.commit()

        return jsonify({
            'header': new_ad.header,
            'description': new_ad.description,
            'date': new_ad.date
        })

    def delete(self, ad_id):

        remove_add = AdModel.query.filter_by(ad_id)
        db.session.remove(remove_add)
        db.commit




app.add_url_rule('/new_user', view_func=AdView.as_view('create_user'), methods=['POST'])
app.add_url_rule('/get_ad/<int:ad_id>', view_func=AdView.as_view('get_ad'), methods=['GET'])
app.add_url_rule('/delete_ad/<int:ad_id>', view_func=AdView.as_view('del_ad'),methods=['DELETE'])
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
