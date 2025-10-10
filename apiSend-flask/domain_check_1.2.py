from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Please enter a link to check"

TRUSTED_DOMAINS = [".edu", ".gov"]

@app.route("/check/<path:link>")
def trustworthy_check(link):
    for domain in TRUSTED_DOMAINS:
        if domain in link:
            return jsonify({"link": link, "trusted": True})
    return jsonify({"link": link, "trusted": False})

if __name__ == "__main__":
    app.run(port=5000, debug=True)  # <-- different port (5001)
