from flask import Flask, render_template, request

app = Flask(__name__)

#create a list to store data
submissions = []

# Home route (main page of your site)
@app.route('/')
def home():
    return render_template('index.html')


# Create a list to store unavailability data
unavailability_list = []

@app.route('/submit', methods=['POST'])
def submit():
    # Get the data from the form
    name = request.form['name']  # This gets the name input
    unavailability = request.form['unavailability']  # This gets the availability input

    #stores info into data
    submissions.append({'name' : name, 'unavailability' : unavailability})

    # Print the data to the terminal for now
    print(submissions)
    
    # For now, we'll just return a success message
    return render_template('unavailability.html', submissions = submissions)


@app.route('/unavailability')
def show_unavailability():
    return render_template('unavailability.html', data=unavailability_list)


if __name__ == '__main__':
    app.run(debug=True)
