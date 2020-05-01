import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)


def WriteToFile(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def WriteToCSV(data):
    with open('database.csv', 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(database2, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        WriteToCSV(data)
        return redirect('/thankyou.html')
    else:
        return 'something wrong ! Try again'
