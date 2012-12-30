from flask import Flask
from deapi.blueprints.pts import pts

app = Flask(__name__)
app.register_blueprint(pts, url_prefix='/pts')

if __name__ == "__main__":
    app.run(debug=True)
