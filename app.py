from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,IntegerField, SelectField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

class MyForm(FlaskForm):
    name = StringField('First Name', validators=[InputRequired()])
    name1 = StringField('Last Name', validators=[InputRequired()])
    Address = TextAreaField('Address')
    phone = IntegerField('Phone')
    selects = SelectField('Select', choices=[('Trial', 'Trial'), ('Regular', 'Regular'), ('Premium', 'Premium')])

@app.route('/', methods=['GET', 'POST'])
def form():
    form = MyForm()

    if form.validate_on_submit():
        return render_template('results.html', name=form.name.data, name1=form.name1.data, Address=form.Address.data, phone=form.phone.data , selects=form.selects.data)
    return render_template('form.html', form=form)



@app.route("/home")
def home():
    return render_template("SubscriptionPage.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thanks.html")




if __name__ == '__main__':
    app.run(port='80')

