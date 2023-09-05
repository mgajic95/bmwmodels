from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from fuzzywuzzy import fuzz

app = Flask(__name__)

user_data = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username from the form
        username = request.form['usernameInput']

        # Check if the username is not empty
        if username:
            # Store the username in the session or database
            user_data['username'] = username

            # Redirect to the personalized page with the username parameter
            return redirect(url_for('personalized', user_name=username))

    return render_template('sign_in.html')


@app.route('/logout')
def logout():
    # Clear the stored user data when logging out
    user_data.clear()
    return redirect('/')


@app.route('/personalized/<user_name>')
@app.route('/personalized', defaults={'user_name': 'Guest'})
def personalized(user_name):
    return render_template('personalized.html', user_name=user_name)

@app.route('/bmwlist')
def bmwlist():
    return render_template('bmwlist.html')



@app.route('/e28')
def bmw28():
    return render_template('e28.html')

@app.route('/e34')
def bmw34():
    return render_template('e34.html')

@app.route('/e39')
def bmw39():
    return render_template('e39.html')

@app.route('/e60')
def bmw60():
    return render_template('e60.html')

@app.route('/f10')
def bmw10():
    return render_template('f10.html')

@app.route('/series1')
def series1():
    return render_template('series1.html')

@app.route('/series2')
def series2():
    return render_template('series2.html')
@app.route('/series3')
def series3():
    return render_template('series3.html')
@app.route('/series4')
def series4():
    return render_template('series4.html')
@app.route('/series5')
def series5():
    return render_template('series5.html')
@app.route('/series6')
def series6():
    return render_template('series6.html')
@app.route('/series7')
def series7():
    return render_template('series7.html')
@app.route('/series8')
def series8():
    return render_template('series8.html')



if __name__ == '__main__':
    app.run(debug=True)