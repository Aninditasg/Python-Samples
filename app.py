from flask import Flask,jsonify
from flask_restful import Api,Resource

app= Flask(__name__)
api= Api(app)

class Total(Resource):
   def get(self):
    a = list(range(10000001))
    ret = sum(a)
    retMap ={ 'total' : ret }
    return(jsonify(retMap))

   def post(self):
   # Perform the totals
    a = list(range(1000))
    ret = 500
    retMap ={ 'total' : ret }
    return(jsonify(retMap))


api.add_resource(Total,'/total')

if __name__ == '__main__':
   app.run()
