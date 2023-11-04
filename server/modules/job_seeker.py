from __main__ import app
from flask import request
from flask_pymongo import PyMongo
mongo = PyMongo(app)
from bson import ObjectId

@app.route('/jobSeeker', methods=['POST', 'GET'])
def get_job_seeker():
    data = request.get_json()

    job_seeker_id = data.get('jobSeekerId')
    job_seeker = mongo.db.jobseekers.find_one_or_404({"_id": ObjectId(job_seeker_id)})
    job_seeker['_id'] = str(job_seeker['_id'])

    return job_seeker


@app.route('/jobSeekers', methods=['POST'])
def get_job_seekers():
    job_seekers = list(mongo.db.jobseekers.find())
    for job_seeker in job_seekers:
        job_seeker['_id'] = str(job_seeker['_id'])

    return job_seekers


@app.route('/updateJobSeeker', methods=['POST'])
def update_job_seeker():
    data = request.get_json()

    job_seeker_id = data.get('jobSeekerId')
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    gender = data.get('gender')
    country = data.get('country')
    job_title = data.get('jobTitle')
    company_name = data.get('companyName')
    recent_exp = data.get('recentExp')
    recent_edu = data.get('recentEdu')

    job_seeker = {}

    if first_name:
        job_seeker['firstName'] = first_name
    if last_name:
        job_seeker['lastName'] = last_name
    if gender:
        job_seeker['gender'] = gender
    if country:
        job_seeker['country'] = country
    if job_title:
        job_seeker['jobTitle'] = job_title
    if company_name:
        job_seeker['companyName'] = company_name
    if recent_exp:
        job_seeker['recentExperience'] = recent_exp
    if recent_edu:
        job_seeker['recentEducation'] = recent_edu
    
    mongo.db.jobseekers.update_one(
        {"_id": ObjectId(job_seeker_id)}, {"$set": job_seeker})

    return "Job seeker updated."