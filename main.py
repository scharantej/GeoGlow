
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the routes for the application
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about-us')
def about():
    return render_template('about_us.html')

@app.route('/contact-us', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('contact_us.html')

# Main driver function
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
