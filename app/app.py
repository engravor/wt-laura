#!flask/bin/python
import requests
from flask import Flask, request, abort, jsonify, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

combinations = [
  ["first_name", "last_name", "birth_date"], 
  ["first_name", "last_name", "id"], 
  ["first_name", "last_name", "id", "birth_date"], 
  ["id", "birth_date"],
  ["last_name", "id", "birth_date"]
]

def getCombinations(ins):
  #TODO: hit the database to get the correct list of cominations for ins
  return combinations

def instantiate(comb):
  data = {}
  #req_data = request.values
  for val in comb:
    data[val] = request.json['member'][val]
  json_data = json.dumps(data)
  return json_data

@app.route('/wt/api/v1.0/ping',methods=['GET'])
def ping():
    return "Hello, World! It's Working"

@app.route('/wt/api/v1.0/elegible',methods=['POST'])
def elegible():
  if not request.json or not 'trading_partner_id' in request.json:
    abort(400)
    
  #check insurance name  
  ins = request.json['trading_partner_id'];

  #get valid combinations for insurance
  combList = getCombinations(ins);

  success = False
  
  while (len(combList) > 0): 
    #build json
    pokitdokData = instantiate(combList.pop())

    #call pokitdok TODO:extract in a method
    url = 'http://demo4484747.mockable.io/elegible'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(pokitdokData), headers=headers)
    data = r.json()

    if ('reject_reason' not in data):
      success = True
      break
    else:
      reject_reason = data['reject_reason']
      if reject_reason == "invalid_subscriber_insured_name":
        #remove those with name
        combList = [comb for comb in combList if "first_name" not in comb]
      if reject_reason == "invalid_subscriber_insured_id":
        #remove those with name
        combList = [comb for comb in combList if "id" not in comb]
           
  if success:
    response = jsonify( { 'valid_requests': True, 'elegible': data['pharmacy'] } )
    return response
  
  response = jsonify({'valid_requests': False, 'list': combList})
  return response

if __name__ == '__main__':
    app.run(debug=True)
