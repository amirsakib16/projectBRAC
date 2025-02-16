from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
def passwordChecker(pas):
    if len(pas)<5:
        return "Password length is too small"
    elif len(pas)==9:
        return "length is average"
    elif len(pas)>9:
        return "Strong password"
    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/password", methods=["POST"])
def ps():
    data = request.get_json()
    text = data.get("PASS","")
    result = passwordChecker(text)
    return jsonify({"RESPASS":result})
if __name__ == "__main__":
    app.run(debug=True)