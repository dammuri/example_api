from flask_restful import Resource
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
