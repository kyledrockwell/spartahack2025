from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code_input = request.form.get("code")  # Get input from the form
        return f"You entered: {code_input}"  # Display the entered code
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
