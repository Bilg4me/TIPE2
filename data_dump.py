import requests
import json

def parser(aliment):
    r_str = "https://api.edamam.com/api/food-database/v2/parser?app_id=f51553ea&app_key=259110672d1443256dd9226467e0d197&ingr="+aliment+"&nutrition-type=cooking&category=generic-foods"
    r = requests.get(r_str)
    return r

def nutrients(foodId):
    payload = {
      "ingredients": [
        {
          "quantity": 1,
          "measureURI": "http://www.edamam.com/ontologies/edamam.owl#Measure_unit",
          "foodId": foodId
        }
      ]
    }
    
    r = requests.post(url="https://api.edamam.com/api/food-database/v2/nutrients?app_id=47b87bfa&app_key=9c733cd9a790a8985d61a1040fbc01c9", headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, data=json.dumps(payload))

    return r


def ficheTechnique(aliment):
    r0 = parser(aliment)
    if r0.status_code == 200:
        fichedict = r0.json()['parsed'][0]['food']
        foodId,image = (fichedict['foodId'],fichedict['image'])
    r = nutrients(foodId)
    if r.status_code == 200:
        fichedict2 = {key : r.json()[key] for key in ['healthLabels', 'cautions', 'totalNutrients', 'totalDaily', 'totalWeight']}
        return foodId,image,fichedict2
    

