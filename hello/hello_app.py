from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Continuous Integrations. It always seems impossible until its done. - Nelson Mandela"

if __name__ == "__main__":
    app.run()
