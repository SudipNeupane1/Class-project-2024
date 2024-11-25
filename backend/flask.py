from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory list to store submitted data
submitted_data = []

# Change the template folder to 'views'
app.template_folder = 'views'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        age = request.form.get('age')

        # Add submitted data to the list
        submitted_data.append({'name': name, 'age': age})

    # Render the HTML template with the form and submitted data
    return render_template('index.html', submitted_data=submitted_data)

if __name__ == '__main__':
    app.run(debug=False)
