# Flask Registration Form

This is my assignment for the Flask registration form. It's a small web app that shows a form in the browser, takes a name, city and phone number, and then shows a confirmation page with the details that were entered.

## How to run it

You need Python 3 installed. Flask is the only thing you have to install:

```
pip install flask
```

Then, from inside this folder:

```
python app.py
```

(On Mac or Linux you may need `python3` and `pip3`.)

Open your browser and go to **http://127.0.0.1:5000**. Press `Ctrl + C` in the terminal when you want to stop the server.

## What happens when you use it

1. The home page shows the registration form with three fields: Name, City and Phone Number.
2. You fill them in and press **Submit**. The form sends the data to the server with a POST request.
3. If everything looks fine, you get a confirmation page that lists what you entered.
4. If something is missing or wrong, the form shows again with a red message under the field, and whatever you already typed is still there so you don't have to start over.
5. There's a "Register another person" button on the confirmation page to go back to the form.

## Folder structure

```
FlaskForm-YourName/
├── app.py                  # the Flask app and routes
├── templates/
│   ├── register.html       # the form page
│   └── confirmation.html   # the page that shows the submitted details
├── static/
│   └── style.css           # a bit of styling so it doesn't look plain
└── README.md
```

Flask looks for HTML files in a folder called `templates` and for CSS in `static`, so those folder names need to stay the same.

## How the code works

- **`app = Flask(__name__)`** creates the app.
- **`@app.route("/")`** shows the form using `render_template("register.html")`.
- **`@app.route("/register", methods=["POST"])`** receives the submitted form. I read the values with `request.form.get(...)`, check them, and then render the confirmation page.
- **Validation:** name and city can't be empty, and the phone number has to be exactly 10 digits (I used a regular expression for this).
- **Templates:** the HTML files use Jinja placeholders like `{{ name }}` to show the data. Jinja also escapes the text automatically, so someone typing HTML into the form can't break the page. I tested this.
- **`url_for(...)`** is used for links and the form action instead of typing paths by hand.
- If you open `/register` directly in the browser (a GET request), it just sends you back to the form.

## Things I'd improve later

- Save the registrations in a database (I did PostgreSQL in the previous module, so that would be a good next step)
- Allow phone numbers with a country code like +91
- Add an email field

## Problems you might hit

- **`ModuleNotFoundError: No module named 'flask'`**: run `pip install flask` first.
- **Port already in use**: something else is running on port 5000. Close it, or change the last line of `app.py` to `app.run(debug=True, port=5001)`.
- **Template not found**: make sure the `templates` folder is in the same folder as `app.py`.
