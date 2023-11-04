from __main__ import app
from flask import request
from flask_pymongo import PyMongo
mongo = PyMongo(app)
from bson import ObjectId

@app.route('/updateBusiness', methods=['POST'])
def update_business():
    data = request.get_json()

    business_id = data.get('businessId')
    company_name = data.get('companyName')
    registration_number = data.get('registrationNum')
    address = data.get('address')
    background = data.get('companyBackground')
    company_size = data.get('companySize')

    businsess = {}

    if company_name:
        businsess['name'] = company_name
    if registration_number:
        businsess['registrationNumber'] = registration_number
    if address:
        businsess['address'] = address
    if background:
        businsess['background'] = background
    if company_size:
        businsess['companySize'] = company_size

    mongo.db.businesses.update_one(
        {"_id": ObjectId(business_id)}, {"$set": businsess})

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