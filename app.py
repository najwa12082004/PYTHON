from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)
class Marvel(Resource)
  def get(self):
    return {"message": "Hello, World!"} 
api.add_resource(Marvel,'/Najwa')
class captain(Resource):
  def post(self):
    return{"message":"Hello guyyyss"}
if __name__ == '__main__':
 app.run(debug=True)