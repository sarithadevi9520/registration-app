from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    # Render the HTML form
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_form():
    # Get data from the form
    data = request.form
    full_name = data.get("fullName")
    email = data.get("email")
    user_name = data.get("userName")
    phone = data.get("phone")
    password = data.get("password")
    confirm_password = data.get("confirmPassword")
    gender = data.get("gender")

    # Validation logic
    errors = {}
    if not full_name:
        errors["fullName"] = "Full Name is required."
    if not email:
        errors["email"] = "Email is required."
    elif "@" not in email:
        errors["email"] = "Enter a valid email."
    if not phone or len(phone) != 10 or not phone.isdigit():
        errors["phone"] = "Enter a valid 10-digit phone number."
    if len(password) < 6:
        errors["password"] = "Password must be at least 6 characters."
    if password != confirm_password:
        errors["confirmPassword"] = "Passwords do not match."
    if not gender:
        errors["gender"] = "Gender selection is required."

    # Return errors if any
    if errors:
        return jsonify({"status": "error", "errors": errors}), 400

    # If no errors, return success
    return jsonify({"status": "success", "message": "Form submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
