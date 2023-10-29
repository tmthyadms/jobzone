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
    email = request.form.get('email')
    password = request.form.get('password')
    account = request.form.get('account')

    # job seeker additional fields during registration
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')

    # business additional fields during registration
    company_name = request.form.get('company-name')  
    registration_number = request.form.get('registration-number') 

    auth = {
        "email": email,
        "password": password,
        "account": account,
    }

    auth_id = mongo.db.auths.insert_one(auth).inserted_id

    if account == 'Job seeker':
        job_seeker = {}
        job_seeker['_id'] = auth_id

        if first_name:
            job_seeker['firstname'] = first_name
        if last_name:
            job_seeker['lastname'] = last_name

        mongo.db.jobseekers.insert_one(job_seeker).inserted_id
    elif account == 'Business':
        businses_data = {}
        businses_data['_id'] = auth_id

        if company_name:
            businses_data['name'] = company_name
        if registration_number:
            businses_data['registrationnumber'] = registration_number
        
        mongo.db.businesses.insert_one(businses_data).inserted_id

    return str(auth_id)
 
@app.route('/auth', methods=['POST', 'GET'])
def get_auth():
    auth_id = request.form.get('auth-id')
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
    auth_id = request.form.get('auth-id')
    email = request.form.get('email')
    password = request.form.get('password')

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
    auth_id = request.form.get('auth-id')
    auth = mongo.db.auths.find_one_or_404({"_id": ObjectId(auth_id)})

    if auth['account'] == 'Job seeker':
        mongo.db.jobseekers.delete_one({"_id": ObjectId(auth_id)})
    elif auth['account'] == 'Business':
        mongo.db.businesses.delete_one({"_id": ObjectId(auth_id)})

    mongo.db.auths.delete_one({"_id": ObjectId(auth_id)})

    return "Auth deleted."

############################ JOB SEEKERS ############################
#### KEEP IN MIND THAT, JOB SEEKERS IDS ARE ASSOCIATED WITH AUTH ####
@app.route('/jobSeeker', methods=['POST', 'GET'])
def get_job_seeker():
    job_seeker_id = request.form.get('job-seeker-id')
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
    job_seeker_id = request.form.get('job-seeker-id')
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    gender = request.form.get('gender')
    country = request.form.get('country')
    job_title = request.form.get('job-title')
    company_name = request.form.get('company-name')
    education_level = request.form.get('education-level')
    study_field  = request.form.get('study-field')

    job_seeker = {}

    if first_name:
        job_seeker['firstname'] = first_name
    if last_name:
        job_seeker['lastname'] = last_name
    if gender:
        job_seeker['gender'] = gender
    if country:
        job_seeker['country'] = country
    if job_title:
        job_seeker['jobtitle'] = job_title
    if company_name:
        job_seeker['companyname'] = company_name
    if education_level:
        job_seeker['educationlevel'] = education_level
    if study_field:
        job_seeker['studyfield'] = study_field

    mongo.db.jobseekers.update_one({"_id": ObjectId(job_seeker_id)}, {"$set": job_seeker})

    return "Job seeker updated."

############################ BUSINESSES ############################
### KEEP IN MIND THAT, BUSSINSESSES IDS ARE ASSOCIATED WITH AUTH ###
@app.route('/updateBusiness', methods=['POST'])
def update_business():
    business_id = request.form.get('business-id')
    company_name = request.form.get('company-name')
    company_registartion_number = request.form.get('company-registration-number')
    address = request.form.get('address')
    background = request.form.get('company-background')
    company_size = request.form.get('company-size')

    businsess = {}

    if company_name:
        businsess['name'] = company_name
    if company_registartion_number:
        businsess['registrationnumber'] = company_registartion_number
    if address:
        businsess['address'] = address
    if background:
        businsess['background'] = background
    if company_size:
        businsess['companysize'] = company_size

    mongo.db.businesses.update_one({"_id": ObjectId(business_id)}, {"$set": businsess})

    return "Business updated."

@app.route('/business', methods=['POST', 'GET'])
def get_business():
    business_id = request.form.get('business-id')
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
    username = request.form.get('uname')
    password = request.form.get('pwd')

    user = mongo.db.auths.find_one({"username": username, "password": password})

    return str(user)

############################ JOB POSTINGS ############################
@app.route('/createJobPosting', methods=['POST'])
def create_job_posting():
    title = request.form.get('title')
    location = request.form.get('location')
    department = request.form.get('department')
    min_salary_range = request.form.get('min-salary-range')
    max_salary_range = request.form.get('max-salary-range')
    description = request.form.get('description')
    requirements = request.form.get('requirements')
    benefits = request.form.get('benefits')

    job_posting = {
        'title': title,
        'location': location,
        'department': department,
        'minsalaryrange': min_salary_range, 
        'maxsalaryrange': max_salary_range,
        'description': description,
        'requirements': requirements,
        'benefits': benefits,
    }

    job_posting_id = mongo.db.jobpostings.insert_one(job_posting).inserted_id
    return str(job_posting_id)

@app.route('/jobPosting', methods=['POST'])
def get_jobposting():
    job_posting_id = request.form.get('job-posting-id')
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
    job_posting_id = request.form.get('job-posting-id')
    title = request.form.get('title')
    location = request.form.get('location')
    department = request.form.get('department')
    min_salary_range = request.form.get('min-salary-range')
    max_salary_range = request.form.get('max-salary-range')
    description = request.form.get('description')
    requirements = request.form.get('requirements')
    benefits = request.form.get('benefits')

    job_posting = {}

    if title:
        job_posting['title'] = title
    if location:
        job_posting['location'] = location
    if department:
        job_posting['department'] = department
    if min_salary_range:
        job_posting['minsalaryrange'] = min_salary_range
    if max_salary_range:
        job_posting['maxsalaryrange'] = max_salary_range
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
    job_posting_id = request.form.get('job-posting-id')
    mongo.db.jobpostings.delete_one({"_id": ObjectId(job_posting_id)})
    return "Job posting deleted."

if __name__ == "__main__":
    app.run(port=5000, debug=True)

#https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application#step-2-setting-up-forms
#https://medium.com/techcrush/how-to-render-html-file-in-flask-3fbfb16b47f6
#https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/