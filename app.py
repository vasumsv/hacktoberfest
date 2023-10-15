from flask import Flask, render_template, request

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    # You can process the data or perform any required actions here
    # For this example, let's just print the data
    print(f"Received data - Name: {name}, Email: {email}")
    
    return "Data received successfully!"

if __name__ == '__main__':
    app.run(debug=True)


Install Flask if you haven't already:
Copy code
pip install flask
Run the Flask application:
Copy code
python app.py
