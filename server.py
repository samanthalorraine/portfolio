# you cal never call a file f/Flask.py

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__) # using the Flask  class in flask to intaticiate an app (__name__)
print(__name__) # when printed  __maine__ is printed


@app.route('/') 
def my_home():
    return render_template("index.html")

# about
@app.route('/<string:page_name>') 
def html_page(page_name):
    return  render_template(page_name)



def write_to_file(data):
    with open ("database.txt", mode = "a") as database:
        email = data['email']
        subject= data['subject']
        message = data['message']
        file=database.write(f"\n{email},\n{subject},\n{message}")


def write_to_csv(data):
    with open ("database.csv", mode = "a", newline="") as database2:
        email = data['email']
        subject= data['subject']
        message = data['message']
        csv_writer=csv.writer(database2, delimiter = ",", quotechar = " ", quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        try: 
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except: 
            return "did not save to database"
    else:
        return " something went wrong try again :("



#https://github.com/samanthalorraine/portfolio.git
#$env:FLASK_APP = "server.py"

#$env:FLASK_ENV = "development"   .. puts debug mode on .. makes it easier to edit and see reulstod codeon website
#flask run
# alwayscd








