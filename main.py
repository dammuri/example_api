from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)

param_args = reqparse.RequestParser()
param_args.add_argument('name',type=str,help="name should be fulfilled",required=True)
param_args.add_argument('ether',type=str, help="etheraddress should be filled", required=True)
param_args.add_argument('ammount',type=int,default=0)

param_args_update = reqparse.RequestParser()
param_args_update.add_argument('name',type=str)
param_args_update.add_argument('ether',type=str)
param_args_update.add_argument('ammount',type=int)

class get_data(Resource):
    def get(self):
        output =[]
        data = wallet.query.all()
        for get_data in data:
            datas = {"id":get_data.id,
                "name" : get_data.name,
                "etheraddress":get_data.ether,
                "ammount":get_data.ammount}
            output.append(datas)
        return {"person":output}


class wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    ether=db.Column(db.String(45),nullable=False)
    ammount=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"id : {self.id}, nama:{self.name}, etheraddress:{self.ether}, ammount:{self.ammount}"


class WalletRoute(Resource):
    def get(self,id):
        query = wallet.query.filter_by(id=id).first()
        if not query:
            abort(404,message="not found data")
        return {"id":query.id, "nama":query.name,"etheraddress":query.ether,"ammount":query.ammount}
    
    def put(self,id):
        query = wallet.query.filter_by(id=id).first()
        argument = param_args.parse_args()
        if not query:
            data = wallet(name=argument['name'],ether=argument['ether'],ammount=argument['ammount'])
            db.session.add(data)
            db.session.commit()
            return {"message":"data added"}
        return {"message":"data exist"}
    
    def patch(self,id):
        query = wallet.query.filter_by(id=id).first()
        param = param_args_update.parse_args()
        if not query:
            abort(404,message="data not exist")
        if param['name']:
            query.name = param['name']
        if param['ether']:
            query.ether=param['ether']
        if param['ammount']:
            query.ammount=param['ammount']
        db.session.commit()
        return {"message":"data updated"}

api.add_resource(WalletRoute, "/data/<int:id>")
api.add_resource(get_data,'/data')
if __name__ == '__main__':
    app.run(debug=True)