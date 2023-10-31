from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/jobzone"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

############################ AUTH ############################
@app.route('/createAuth', methods=['POST'])
def create_auth():
    # mandatory fields for both
    data = request.get_json()

    auth = data.get('common')
    auth_id = mongo.db.auths.insert_one(auth).inserted_id

    if auth.accountType == 'Job seeker':
        job_seeker = data.get('jobSeeker')
        mongo.db.jobseekers.insert_one(job_seeker)
    elif auth.accountType == 'Business':
        business = data.get('business')
        mongo.db.businesses.insert_one(business)

    return str(auth_id)
 
@app.route('/auth', methods=['POST', 'GET'])
def get_auth():
    data = request.get_json()
    auth_id = data.get('auth-id')
    auth = mongo.db.auths.find_one_or_404({"_id": ObjectId(auth_id)})
    auth['_id'] = str(auth['_id'])
    return render_template('auth.html', auth=auth)

@app.route('/auths', methods=['POST'])
def get_auths():
    auths = list(mongo.db.auths.find())
    for auth in auths:
        auth['_id'] = str(auth['_id'])
    return render_template('auths.html', auths=auths)

@app.route('/updateAuth', methods=['POST'])
def update_auth():
    data = request.get_json()

    auth_id = data.get('auth-id')
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

    auth_id = data.get('auth-id')
    auth = mongo.db.auths.find_one_or_404({"_id": ObjectId(auth_id)})

    if auth['accountType'] == 'Job seeker':
        mongo.db.jobseekers.delete_one({"_id": ObjectId(auth_id)})
    elif auth['accountType'] == 'Business':
        mongo.db.businesses.delete_one({"_id": ObjectId(auth_id)})

    mongo.db.auths.delete_one({"_id": ObjectId(auth_id)})

    return "Auth deleted."

############################ JOB SEEKERS ############################
#### KEEP IN MIND THAT, JOB SEEKERS IDS ARE ASSOCIATED WITH AUTH ####
@app.route('/jobSeeker', methods=['POST', 'GET'])
def get_job_seeker():
    data = request.get_json()

    job_seeker_id = data.get('job-seeker-id')
    job_seeker = mongo.db.jobseekers.find_one_or_404({"_id": ObjectId(job_seeker_id)})
    job_seeker['_id'] = str(job_seeker['_id'])
    return render_template('jobseeker.html', job_seeker=job_seeker)

@app.route('/jobSeekers', methods=['POST'])
def get_job_seekers():
    job_seekers = list(mongo.db.jobseekers.find())
    for job_seeker in job_seekers:
        job_seeker['_id'] = str(job_seeker['_id'])
    return render_template('jobseekers.html', job_seekers=job_seekers)

@app.route('/updateJobSeeker', methods=['POST'])
def update_job_seeker():
    data = request.get_json()

    job_seeker_id = data.get('job-seeker-id')
    first_name = data.get('first-name')
    last_name = data.get('last-name')
    gender = data.get('gender')
    country = data.get('country')
    job_title = data.get('job-title')
    company_name = data.get('company-name')
    education_level = data.get('education-level')
    study_field  = data.get('study-field')

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
    if education_level:
        job_seeker['educationLevel'] = education_level
    if study_field:
        job_seeker['studyField'] = study_field

    mongo.db.jobseekers.update_one({"_id": ObjectId(job_seeker_id)}, {"$set": job_seeker})

    return "Job seeker updated."

############################ BUSINESSES ############################
### KEEP IN MIND THAT, BUSSINSESSES IDS ARE ASSOCIATED WITH AUTH ###
@app.route('/updateBusiness', methods=['POST'])
def update_business():
    data = request.get_json()

    business_id = data.get('business-id')
    company_name = data.get('company-name')
    company_registration_number = data.get('company-registration-number')
    address = data.get('address')
    background = data.get('company-background')
    company_size = data.get('company-size')

    businsess = {}

    if company_name:
        businsess['name'] = company_name
    if company_registration_number:
        businsess['registrationNumber'] = company_registration_number
    if address:
        businsess['address'] = address
    if background:
        businsess['background'] = background
    if company_size:
        businsess['companySize'] = company_size

    mongo.db.businesses.update_one({"_id": ObjectId(business_id)}, {"$set": businsess})

    return "Business updated."

@app.route('/business', methods=['POST', 'GET'])
def get_business():
    data = request.get_json()
    business_id = data.get('business-id')
    business = mongo.db.businesses.find_one_or_404({"_id": ObjectId(business_id)})
    business['_id'] = str(business['_id'])
    return render_template('business.html', business=business)

@app.route('/businesses', methods=['POST'])
def get_businesses():
    businesses = list(mongo.db.businesses.find())
    for business in businesses:
        business['_id'] = str(business['_id'])
    return render_template('businesses.html', businesses=businesses)

############################ LOGIN ############################
#TODO: set session or access token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = mongo.db.auths.find_one({"email": email, "password": password})

    return str(user)

############################ JOB POSTINGS ############################
@app.route('/createJobPosting', methods=['POST'])
def create_job_posting():
    data = request.get_json()

    title = data.get('title')
    location = data.get('location')
    department = data.get('department')
    min_salary_range = data.get('min-salary-range')
    max_salary_range = data.get('max-salary-range')
    description = data.get('description')
    requirements = data.get('requirements')
    benefits = data.get('benefits')

    job_posting = {
        'title': title,
        'location': location,
        'department': department,
        'minSalaryRange': min_salary_range, 
        'maxSalaryRange': max_salary_range,
        'description': description,
        'requirements': requirements,
        'benefits': benefits,
    }

    job_posting_id = mongo.db.jobpostings.insert_one(job_posting).inserted_id
    return str(job_posting_id)

@app.route('/jobPosting', methods=['POST'])
def get_jobposting():
    data = request.get_json()

    job_posting_id = data.get('job-posting-id')
    job_posting = mongo.db.jobpostings.find_one_or_404({"_id": ObjectId(job_posting_id)})
    job_posting['_id'] = str(job_posting['_id'])
    return render_template('jobposting.html', job_posting=job_posting)

@app.route('/jobPostings', methods=['POST'])
def get_jobpostings():
    job_postings = list(mongo.db.jobpostings.find())
    for job_posting in job_postings:
        job_posting['_id'] = str(job_posting['_id'])
    return render_template('jobpostings.html', job_postings=job_postings)

@app.route('/updateJobPosting', methods=['POST'])
def update_job_posting():
    data = request.get_json()

    job_posting_id = data.get('job-posting-id')
    title = data.get('title')
    location = data.get('location')
    department = data.get('department')
    min_salary_range = data.get('min-salary-range')
    max_salary_range = data.get('max-salary-range')
    description =data.get('description')
    requirements = data.get('requirements')
    benefits = data.get('benefits')

    job_posting = {}

    if title:
        job_posting['title'] = title
    if location:
        job_posting['location'] = location
    if department:
        job_posting['department'] = department
    if min_salary_range:
        job_posting['minSalaryRange'] = min_salary_range
    if max_salary_range:
        job_posting['maxSalaryRange'] = max_salary_range
    if description:
        job_posting['description'] = description
    if requirements:
        job_posting['requirements'] = requirements
    if benefits:
        job_posting['benefits'] = benefits

    mongo.db.jobpostings.update_one({"_id": ObjectId(job_posting_id)}, {"$set": job_posting})
    return "Job posting updated."

@app.route('/deleteJobPosting', methods=['POST'])
def delete_job_posting():
    data = request.get_json()

    job_posting_id = data.get('job-posting-id')
    mongo.db.jobpostings.delete_one({"_id": ObjectId(job_posting_id)})
    return "Job posting deleted."

if __name__ == "__main__":
    app.run(port=5000, debug=True)

#https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application#step-2-setting-up-forms
#https://medium.com/techcrush/how-to-render-html-file-in-flask-3fbfb16b47f6
#https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/