from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starsaligned.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications
db = SQLAlchemy(app)  # Initialize SQLAlchemy


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    unavailability = db.relationship('Unavailability', backref='user', lazy=True)

# Unavailability model
class Unavailability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day = db.Column(db.String(2), nullable=False)  # Store the day as "m", "t", etc.


#create database tables
def create_tables():
    db.create_all()


# Home route (main page of your site)
@app.route('/')
def home():
    return render_template('index.html')




@app.route('/submit', methods=['POST'])
def submit():
    # Get the data from the form
    name = request.form['name']  # This gets the name input
    day = request.form['unavailability']  # This gets the availability input

    #create a new user instance
    new_user = User(name = name)

    #for now, unavailability is only M,T,W,Th,F, Sa, Su
    new_unavailability = Unavailability(user=new_user, day=day)

    # add the new user and unavailability to the database
    db.session.add(new_user)
    db.session.add(new_unavailability)
    db.session.commit()  # Commit the session to save changes

    # Print the data to the terminal for now
    print(f'Submission: {name} is unavailable on {day}')
    
    # For now, we'll just return a success message
    return render_template('unavailability.html', name = name, day = day)


#shoe unavailabilty route
@app.route('/unavailability')
def show_unavailability():
    return render_template('unavailability.html')


if __name__ == '__main__':
    with app.app_context():  # Use app context to access database
        create_tables()  # Create tables before starting the app
        
    app.run(debug=True)
