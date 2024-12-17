#%%
from flask import Flask
from flask import  request
from flask_restful import Api, Resource
from flask_cors import CORS
from geopy.geocoders import Nominatim
import json

#%%

app = Flask(__name__)
CORS(app)
# creating an API object
api = Api(app)
class Area_Finder(Resource):
    def post (self):
        pass
        encoded = request.get_json()  # Get base64 data from API
        geolocator = Nominatim(user_agent="geoapiExercises")
        Latitude=encoded["Latitude"]
        Longitude=encoded["Longitude"]
        Latitude=Latitude.replace("['",'' ) 
        Longitude=Longitude.replace("']",'' )         
        location = geolocator.reverse(Latitude+","+Longitude) 
        return('\ngood',str(location))
                
#%%    
    
api.add_resource(Area_Finder,'/Area_Finder')
if __name__ == "__main__":
    app.run(port=5000, debug=True)
    

