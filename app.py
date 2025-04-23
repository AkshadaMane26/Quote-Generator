from flask import Flask, render_template
from quotes.routes import bp as quotes_bp

app = Flask(__name__)

# Register Blueprint for handling quote-related routes
app.register_blueprint(quotes_bp, url_prefix="/quotes")

# Change the home route to render the index page directly
@app.route('/')
def home():
    return render_template("index.html")  # Directly render index.html instead of API message

if __name__ == "__main__":
    app.run(debug=True)
