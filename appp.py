from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Nyamsika Electronic</h1><p>Your Flask app is running.</p>"

if __name__ == "__main__":
    app.run(debug=True)
