from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == "" or password == "":
        flash("Please fill in both fields.")
        return redirect(url_for('index'))
    else:
        # Placeholder for actual login logic, e.g., checking against a database
        flash(f"Logging in as {username}")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
