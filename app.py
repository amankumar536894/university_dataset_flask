from flask import Flask, request, jsonify
from flask import send_from_directory
from project import answer_question

app = Flask(__name__)
@app.route("/", methods=["GET"])

def home():
    return send_from_directory(".", "index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()
        if not question:
            return jsonify({"error": "Question is required"}), 400

        answer = answer_question(question)
        return jsonify({"question": question, "answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)