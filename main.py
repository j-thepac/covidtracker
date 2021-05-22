from flask import Flask,render_template,request,json,jsonify
import requests


app=Flask(__name__)

class CovidDetails:
    def __init(self,confirmed,deceased,recovered):
        self.confirmed=confirmed
        self.deceased=deceased
        self.recovered=recovered


# Out[11]:
# {'notes': '',
#  'active': 289131,
#  'confirmed': 1103844,
#  'migratedother': 1,
#  'deceased': 10656,
#  'recovered': 804056,
#  'delta': {'confirmed': 9591, 'deceased': 129, 'recovered': 26956}}
def get_covid_Data():
    r = requests.get(url="https://api.covid19india.org/state_district_wise.json")
    data=r.json()["Karnataka"]["districtData"]["Bengaluru Urban"]
    return data

@app.route("/",methods=["GET"])
def display():
    if(request.method=='GET'):
        data=get_covid_Data()
        print(data["confirmed"],data["deceased"],data["recovered"])
        return render_template("index.html",
                               confirmed=data["confirmed"],
                               deceased=data["deceased"],
                               recovered=data["recovered"])



#http:/localhost:5000/
if (__name__== "__main__"):
    app.run(host ='0.0.0.0', port = 5000, debug = True)
