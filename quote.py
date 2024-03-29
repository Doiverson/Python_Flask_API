from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


class Quotes(Resource):
    def get(self):
        return {
            'Steve Jobs': {
                'quote': [
                    'Stay hungry',
                    'Details matter, it’s worth waiting to get it right',
                    'In the broadest context, the goal is to seek enlightenment – however you define it'
                ]
            },
            'linus': {
                'quote': ['Talk is cheap. Show me the code.']
            }
        }

    def post(self):
        parser.add_argument('quote', type=str)
        args = parser.parse_args()

        return {
            'status': True,
            'quote': f'{args["quote"]}'
        }


class UpdateQuote(Resource):
    def put(self, id):
        parser.add_argument('quote', type=str)
        args = parser.parse_args()

        return {
            'id': id,
            'status': True,
            'quote': 'The quote numbered {} was updated.'.format(id)
        }


api.add_resource(Quotes, '/quotes')
api.add_resource(UpdateQuote, '/quotes', '/update/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
