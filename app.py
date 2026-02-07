from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Create a route for the home page
@app.route('/')
def home():
    return '<h1>Hello! My Chatbot is Coming Soon!</h1>'

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
