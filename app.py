from flask import Flask
from loop import views  # Import the blueprint module

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Used for flashing messages

# Register the blueprint
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
