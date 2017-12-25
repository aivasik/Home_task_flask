from flask import request

from app.utils import cube
from flask import render_template
from app.forms import RegistrationForm
# from app.validators import name_is_valid, age_is_valid

def index():
    res = cube(12)
    return 'RES: {}'.format(res)

def register():
    if request.method == "POST":
        form = RegistrationForm(request.form)
        form.validate()
        print(form.errors)

    else:
        form = RegistrationForm()
    return render_template(
        'registration.html',
        form=form,
        errors=form.errors
        )

    # age = request.args.get('age')
    # name = request.args.get('name')
    # email = request.args.get('email')
    # errors = {}
    # if not name_is_valid(name):
    #     errors["name"] = "Invalid name: {}".format(name)
    # if not age_is_valid(age):
    #     errors["age"] = "Invalid age: {}".format(age)
    #
    # if errors:
    #     return str(errors)
    # return "{} {} {}".format(age, name, email)
    # #return "REGISTER"
