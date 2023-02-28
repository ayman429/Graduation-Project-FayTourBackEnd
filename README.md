# Graduation-Project-FayTourBackEnd
Build a Backend Rest API with Python and Django Framework 

## Setup
1. Ensure you have python3 installed
2. Clone the repository
3. create a virtual environment using `virtualenv venv`
4. Activate the virtual environment by running `source venv\Scripts\activate`
5. Install the dependencies using `pip install -r requirements.txt`
6. Migrate existing db tables by running `python manage.py migrate`
7. Run the django development server using `python manage.py runserver`

## User EndPoints
- Registration     `rest-auth/registration/`
- Login            `rest-auth/login/`
- Logout           `rest-auth/logout/`
- Get User         `rest-auth/user/`
- Change Password  `rest-auth/password/change/`
- Reset Password   `password-reset/`