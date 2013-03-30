from flask import Flask
from deapi.blueprints.pts import pts, bts

app = Flask(__name__)
app.register_blueprint(pts, url_prefix='/pts')
app.register_blueprint(bts, url_prefix='/bts')

if __name__ == "__main__":
    app.run(debug=True)
