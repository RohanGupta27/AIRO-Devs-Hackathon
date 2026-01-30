from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/plan", methods=["POST"])
def plan():
    data = request.json
    hours = int(data["hours"])
    task = data["task"].lower()

    plans = []

    if "study" in task:
        plans.append(f"Study for {hours-1} hours and revise for 1 hour.")

    if "revision" in task or "revise" in task:
        plans.append(f"Revise important topics for {hours} hours.")

    if "assignment" in task:
        plans.append(f"Spend {hours-2} hours writing and 2 hours reviewing.")

    if not plans:
        plans.append("Please enter study, revision, or assignment.")

    result = " ".join(plans)   # ✅ result is ALWAYS defined
    return jsonify({"plan": result})




if __name__ == "__main__":
    app.run(debug=True)
