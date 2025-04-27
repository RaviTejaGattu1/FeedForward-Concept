from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Dummy data for statistics
stats = {
    "food_delivered": "10,000 kg",
    "kcal_met": "5M kcal",
    "lives_impacted": "1,000"
}

@app.route('/')
def home():
    return render_template('home.html', stats=stats)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login_user')
def login_user():
    return render_template('login_user.html')

@app.route('/login_admin')
def login_admin():
    return render_template('login_admin.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/provide')
def provide():
    return render_template('provide.html')

@app.route('/request')
def request():
    return render_template('request.html')

@app.route('/search_results')
def search_results():
    # Dummy food listings
    listings = [
        {"name": "Fresh Bread", "images": ["bread1.jpg", "bread2.jpg"], "address": "123 Main St", "distance": "2 km", "freshness": "High"},
        {"name": "Vegetable Soup", "images": ["soup1.jpg"], "address": "456 Oak Ave", "distance": "5 km", "freshness": "Medium"}
    ]
    return render_template('search_results.html', listings=listings)

@app.route('/reserved')
def reserved():
    return render_template('reserved.html')

@app.route('/provider_notification')
def provider_notification():
    return render_template('provider_notification.html')

if __name__ == '__main__':
    app.run(debug=True)
