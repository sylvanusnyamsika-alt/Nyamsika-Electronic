import webbrowser
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <body style='background: linear-gradient(to right, #74ebd5, #ACB6E5); text-align:center; font-family:Arial;'>
        <h1 style='font-size:50px; color:white;'>Nyamsika Electronic</h1>
        <div style='margin-top:50px;'>
            <a href='/video'><button style='width:200px; height:60px; font-size:20px; margin:15px;'>🎥 Video</button></a>
            <a href='/tutorial'><button style='width:200px; height:60px; font-size:20px; margin:15px;'>📘 Tutorial</button></a>
        </div>
    </body>
    """

@app.route("/video")
def video():
    return "<h1 style='text-align:center;'>Video Section</h1>"

@app.route("/tutorial")
def tutorial():
    return "<h1 style='text-align:center;'>Tutorial Section</h1>"

if __name__ == "__main__":
    app.run(debug=True)
