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

    if session['authId']:
        return 'You are currently logged into your active account.'
    else:
        if auth: session['authId'] = auth['_id']
        else: return 'User not found.'

    return 'Login successful.'

@app.route('/logout', methods=['POST'])
def logout():
    if session['authId']: session['authId'] = None
    else: return 'You are not currently signed in.'
    
    return 'Logout successful.'

@app.route('/createAuth', methods=['POST'])
def create_auth():
    # mandatory fields for both
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

        first_name = data.get('firstName')
        last_name = data.get('lastName')
        gender = data.get('gender')
        country = data.get('country')
        recent_exp = data.get('recentExp')
        recent_edu = data.get('recentEdu')

        if first_name:
            job_seeker['firstName'] = first_name
        if last_name:
            job_seeker['lastName'] = last_name
        if gender:
            job_seeker['gender'] = gender
        if country:
            job_seeker['country'] = country
        if recent_exp:
            job_seeker['recentExperience'] = recent_exp
        if recent_edu:
            job_seeker['recentEducation'] = recent_edu

        mongo.db.jobseekers.insert_one(job_seeker).inserted_id
    elif accountType == 'business':
        businses_data = {}
        businses_data['_id'] = auth_id
        company_name = data.get('companyName')
        registration_number = data.get('registrationNum')

        if company_name:
            businses_data['name'] = company_name
        if registration_number:
            businses_data['registrationNum'] = registration_number

        mongo.db.businesses.insert_one(businses_data).inserted_id

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
        if email:
            auth_data['email'] = email
        if password:
            auth_data['password'] = password

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