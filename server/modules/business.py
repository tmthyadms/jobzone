from __main__ import app
from flask import request
from flask_pymongo import PyMongo
mongo = PyMongo(app)
from bson import ObjectId


@app.route('/updateBusiness', methods=['POST'])
def update_business():
    data = request.get_json()

    business_id = data.get('businessId')
    company_name = data.get('compName')
    registration_number = data.get('regNum')
    address = data.get('address')
    company_size = data.get('compSize')

    business = {}

    if company_name: business['name'] = company_name
    if registration_number: business['registrationNumber'] = registration_number
    if address: business['address'] = address
    if company_size: business['companySize'] = company_size

    mongo.db.businesses.update_one({"_id": ObjectId(business_id)}, {"$set": business})

    return "Business updated."


@app.route('/business', methods=['POST', 'GET'])
def get_business():
    data = request.get_json()
    business_id = data.get('businessId')
    business = mongo.db.businesses.find_one_or_404({"_id": ObjectId(business_id)})
    business['_id'] = str(business['_id'])

    return business


@app.route('/businesses', methods=['POST'])
def get_businesses():
    businesses = list(mongo.db.businesses.find())
    for business in businesses:
        business['_id'] = str(business['_id'])
        
    return businesses