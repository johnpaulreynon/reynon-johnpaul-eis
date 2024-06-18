from flask import Flask,render_template, request,redirect
from users import Users
from employee import Employee

app = Flask(__name__)
app.secret_key ="Paul"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form["username"]
    password = request.form["password"]

    result = Users.check_user(username,password)

    if result:
        return redirect('/employee-list')
    else:
        return render_template('login.html')

@app.route('/employee-list')
def employee_list():
    employees = Employee.get_all()
    return render_template('employee_list.html', employees=employees)

@app.route('/add-form')
def add_form():
    return render_template('add_employee.html')
    
@app.route('/add-employee')
def add_employees():
    emp_id = request.form["emp_id"]
    lname = request.form["lname"]
    fname = request.form["fname"]
    mname = request.form["mname"]

    success = Employees.add_employee(emp_id,lname, fname, mname)

    if success:
        session["message"] = "Successfully added"
    else:
         session["message"] = "Failed to add employee"
    
    redirect('/employee-list')

    if __name__ == '__main__':
        app.run()