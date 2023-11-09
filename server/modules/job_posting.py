from __main__ import app
from flask import request, jsonify
from flask_pymongo import PyMongo
mongo = PyMongo(app)
from bson import ObjectId


@app.route('/createJobPosting', methods=['POST'])
def create_job_posting():
    data = request.get_json()

    business_id = data.get('bizId') 
    title = data.get('title')
    location = data.get('location')
    department = data.get('department')
    min_salary_range = data.get('salaryRange').get('min')
    max_salary_range = data.get('salaryRange').get('max')
    description = data.get('desc')
    requirements = data.get('requirements')
    benefits = data.get('benefits')
    #TODO: telecommuting tukar
    telecommuting = False 
    has_business_logo = False 
    has_questions = False 
    employment_type = data.get('employmentType')
    required_experience = data.get('requiredExp')
    required_education = data.get('requiredEdu')
    industry = data.get('industry')
    function = data.get('function')

    job_posting = {
        'title': title,
        'location': location,
        'department': department,
        'salaryRange': {
            'min': min_salary_range,
            'max': max_salary_range
        }, 
        'description': description,
        'requirements': requirements,
        'benefits': benefits,
        'telecommuting': telecommuting,
        'hasBusinessLogo': has_business_logo, 
        'hasQuestions': has_questions, 
        'employmentType': employment_type,
        'requiredExperience': required_experience,
        'requiredEducation': required_education, 
        'industry': industry,
        'function': function,
        'businessId': business_id 
    }

    job_posting_id = mongo.db.jobpostings.insert_one(job_posting).inserted_id

    business = mongo.db.businesses.find_one({ "_id": ObjectId(business_id) })
    
    if 'telecommuting' in job_posting and job_posting['telecommuting'] is False:
      job_posting['telecommuting'] = 0
    elif 'telecommuting' in job_posting and job_posting['telecommuting'] is True:
      job_posting['telecommuting'] = 1

    if 'hasBusinessLogo' in job_posting and job_posting['hasBusinessLogo'] is False:
      job_posting['hasBusinessLogo'] = 0
    elif 'telecommuting' in job_posting and job_posting['telecommuting'] is True:
      job_posting['hasBusinessLogo'] = 1

    if 'hasQuestions' in job_posting and job_posting['hasQuestions'] is False:
      job_posting['hasQuestions'] = 0
    elif 'hasQuestions' in job_posting and job_posting['hasQuestions'] is True:
      job_posting['hasQuestions'] = 1

    job_posting['businessProfile'] = business['businessProfile']
    job_posting.pop('businessId', None)

    print(job_posting)

    return str(job_posting_id)


@app.route('/jobPosting', methods=['POST'])
def get_jobposting():
    data = request.get_json()

    job_posting_id = data.get('jobPostingId')
    job_posting = mongo.db.jobpostings.find_one_or_404({"_id": ObjectId(job_posting_id)})
    job_posting['_id'] = str(job_posting['_id'])

    return job_posting


@app.route('/jobPostings', methods=['POST'])
def get_jobpostings():
    data = request.get_json()
    business_id = data.get('bizId')

    if business_id:
        job_postings = list(mongo.db.jobpostings.find({'businessId': business_id}))
    else:
        job_postings = list(mongo.db.jobpostings.find())

    for job_posting in job_postings:
        job_posting['_id'] = str(job_posting['_id'])

    return job_postings


@app.route('/updateJobPosting', methods=['POST'])
def update_job_posting():
    data = request.get_json()

    job_posting_id = data.get('jobPostingId')
    title = data.get('title')
    location = data.get('location')
    department = data.get('department')
    min_salary_range = data.get('salaryRange').get('min')
    max_salary_range = data.get('salaryRange').get('max')
    description = data.get('desc')
    requirements = data.get('requirements')
    benefits = data.get('benefits')
    employment_type = data.get('employmentType')
    required_experience = data.get('requiredExp')
    required_education = data.get('requiredEdu')
    industry = data.get('industry')
    function = data.get('function')

    job_posting = {}
    job_posting['salaryRange'] = {}
    job_posting['salaryRange']['min'] = ''
    job_posting['salaryRange']['max'] = ''

    if title: job_posting['title'] = title
    if location: job_posting['location'] = location
    if department: job_posting['department'] = department
    if min_salary_range: job_posting['salaryRange']['min'] = min_salary_range
    if max_salary_range: job_posting['salaryRange']['max'] = max_salary_range
    if description: job_posting['description'] = description
    if requirements: job_posting['requirements'] = requirements
    if benefits: job_posting['benefits'] = benefits 
    if employment_type: job_posting['employmentType'] = employment_type  
    if required_experience: job_posting['requiredExperience'] = required_experience  
    if required_education: job_posting['requiredEducation'] = required_education  
    if industry: job_posting['industry'] = industry  
    if function: job_posting['function'] = function       
   
    mongo.db.jobpostings.update_one({"_id": ObjectId(job_posting_id)}, {"$set": job_posting})
    
    return "Job posting updated."


@app.route('/deleteJobPosting', methods=['POST'])
def delete_job_posting():
    data = request.get_json()

    job_posting_id = data.get('jobPostingId')
    mongo.db.jobpostings.delete_one({"_id": ObjectId(job_posting_id)})

    return "Job posting deleted."