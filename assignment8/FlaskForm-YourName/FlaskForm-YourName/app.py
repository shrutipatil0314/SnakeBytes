# Flask Registration Form


import re
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    """Show the empty registration form."""
    return render_template("register.html", errors={}, form={})


@app.route("/register", methods=["POST"])
def register():
    """Handle the form submission."""
    name = request.form.get("name", "").strip()
    city = request.form.get("city", "").strip()
    phone = request.form.get("phone", "").strip()

   
    errors = {}
    if not name:
        errors["name"] = "Please enter your name."
    if not city:
        errors["city"] = "Please enter your city."
    if not re.fullmatch(r"\d{10}", phone):
        errors["phone"] = "Phone number must be exactly 10 digits."

    if errors:
        form = {"name": name, "city": city, "phone": phone}
        return render_template("register.html", errors=errors, form=form), 400

   
    return render_template("confirmation.html", name=name, city=city, phone=phone)


@app.route("/register", methods=["GET"])
def register_redirect():
    """If someone opens /register directly, send them back to the form."""
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
