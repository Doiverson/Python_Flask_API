from flask import Flask, abort, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = [
    {"id": "123jklj213hkl21", "name": "Sho", "country": "Japan"},
    {"id": "123jkljfdsafakl21", "name": "Cony", "country": "Canada"},
    {"id": "123gfdsglj213hkl21", "name": "Natsu", "country": "USA"},
    {"id": "gfd3jklj213hkl21", "name": "Tsumu", "country": "Hawaii"},
]


class User(Resource):
    def get(self):

        id = request.args.get('id')
        result = [n for n in users if n["id"] == id]

        if len(result) >= 1:
            return result[0]
        else:
            abort(404)

    def post(self):

        users.append(request.json)

        return '', 204

    def put(self):

        user = request.json
        lst = [val for val in users if val["id"] == user["id"]]

        if len(lst) >= 1:
            lst[0]["name"] = user["name"]
            lst[0]["age"] = user["age"]
        else:
            abort(404)

        return '', 204

    def delete(self):

        id = request.args.get('id')
        lst = [i for i, val in enumerate(users) if val["id"] == id]
        for index in lst:
            del users[index]

        if len(lst) >= 1:
            return '', 204
        else:
            abort(404)


class AllUsers(Resource):
    def get(self):
        return users


api.add_resource(User, '/user')
api.add_resource(AllUsers, '/users')


if __name__ == "__main__":
    app.run(debug=True)
