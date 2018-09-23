from flask import Flask, render_template, request, redirect, session, flash
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    try:
        session['name']
        session['comments']
    except KeyError:
        session['name'] = None
        session['comments'] = None
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/process', methods=['POST'])
def successful():
    error = False

    if len(request.form['name']) == 0:
        flash('You name must enter a name')
        error = True

    if len(request.form['comments']) == 0:
        flash('Please enter comments')
        error = True

    if len(request.form['comments']) > 120:
        flash('Max characters of 120 is exceeded')
        error = True

    if error is True:
        return redirect('/')

    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comments'] = request.form['comments']
        print('Name: ', session['name'])
        print('Location: ', session['location'])
        print('Language: ', session['language'])
        print('Comments: ', session['comments'])
        return redirect('/result')


@app.route('/danger')
def nope():
    print('\n')
    print('a user tired to visit/danger. we have redirected the user to /')
    print('\n')
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
