from __main__ import app
from flask import request, session
from flask_pymongo import PyMongo
mongo = PyMongo(app)
from bson import ObjectId


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    auth = mongo.db.auths.find_one({"email": email, "password": password})

    if 'authId' in session and session['authId']:
        return 'You are currently logged into your active account.'
    else:
        if auth: session['authId'] = auth['_id']
        else: return ''

    return str(auth['_id'])


@app.route('/logout', methods=['POST'])
def logout():
    if 'authId' in session and session['authId']: session['authId'] = None
    else: return None
    
    return True


@app.route('/createAuth', methods=['POST'])
def create_auth():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    accountType = data.get('accType')

    auth = {
        "email": email,
        "password": password,
        "accountType": accountType,
    }

    auth_id = mongo.db.auths.insert_one(auth).inserted_id

    if accountType == 'job-seeker':
        job_seeker = {}
        job_seeker['_id'] = auth_id
        job_seeker['name'] = {}
        job_seeker['recentExperience'] = {}
        job_seeker['recentEducation'] = {}
        first_name = data.get('name').get('first')
        last_name = data.get('name').get('last')
        gender = data.get('gender')
        country = data.get('country')
        job_title = data.get('recentExp').get('jobTitle')
        company = data.get('recentExp').get('company')
        level_edu = data.get('recentEdu').get('levelEdu')
        field_study = data.get('recentEdu').get('fieldStudy')       

        if first_name: job_seeker['name']['first'] = first_name
        if last_name: job_seeker['name']['last'] = last_name
        if gender: job_seeker['gender'] = gender
        if country: job_seeker['country'] = country
        if job_title: job_seeker['recentExperience']['jobTitle'] = job_title
        if company: job_seeker['recentExperience']['company'] = company
        if level_edu: job_seeker['recentEducation']['levelEducation'] = level_edu
        if field_study: job_seeker['recentEducation']['fieldStudy'] = field_study     

        mongo.db.jobseekers.insert_one(job_seeker).inserted_id
    elif accountType == 'business':
        business = {}
        business['_id'] = auth_id
        company_name = data.get('compName')
        registration_number = data.get('regNum')
        address = data.get('address')
        company_size = data.get('compSize')
        
        if company_name: business['name'] = company_name
        if registration_number:business['registrationNumber'] = registration_number
        if address: business['address'] = address
        if company_size: business['companySize'] = company_size

        mongo.db.businesses.insert_one(business).inserted_id

    return str(auth_id)


@app.route('/auth', methods=['POST', 'GET'])
def get_auth():
    data = request.get_json()

    auth_id = data.get('authId')
    auth = mongo.db.auths.find_one_or_404({"_id": ObjectId(auth_id)})
    auth['_id'] = str(auth['_id'])

    return auth


@app.route('/auths', methods=['POST'])
def get_auths():
    auths = list(mongo.db.auths.find())

    for auth in auths:
        auth['_id'] = str(auth['_id'])

    return auths


@app.route('/updateAuth', methods=['POST'])
def update_auth():
    data = request.get_json()

    auth_id = data.get('authId')
    email = data.get('email')
    password = data.get('password')

    auth_data = {}

    if auth_id:
        if email: auth_data['email'] = email
        if password: auth_data['password'] = password

    mongo.db.auths.update_one({"_id": ObjectId(auth_id)}, {"$set": auth_data})
    
    return "Auth updated."


@app.route('/deleteAuth', methods=['POST', 'GET'])
def delete_auth():
    data = request.get_json()

    auth_id = data.get('authId')
    auth = mongo.db.auths.find_one_or_404({"_id": ObjectId(auth_id)})
    
    if auth['accountType'] == 'job-seeker':
        mongo.db.jobseekers.delete_one({"_id": ObjectId(auth_id)})
    elif auth['accountType'] == 'business':
        mongo.db.businesses.delete_one({"_id": ObjectId(auth_id)})

    mongo.db.auths.delete_one({"_id": ObjectId(auth_id)})

    return "Auth deleted."