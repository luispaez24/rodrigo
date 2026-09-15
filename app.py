from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from threading import Thread
import smtplib

app = Flask(__name__)

# Database setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Email setup
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rodrigogf825@gmail.com'  # your email   # I need rodrigos email and 16 bit password 
app.config['MAIL_PASSWORD'] = 'rhti lqgx fmxr izon'        # 16-char app password, no spaces
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    service = db.Column(db.String(100))
    date = db.Column(db.String(50))
    message = db.Column(db.Text)

# Async email function
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# Routes
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/FreeEstimate")
def free_estimate():
    return render_template("contact.html")  # reuses contact form

@app.route("/uncle")
def uncle():
    return render_template("uncle.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        # get form data
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        service = request.form["service"]
        date = request.form["date"]
        message = request.form["message"]

        # save to database
        new_appt = Appointment(
            name=name, email=email, phone=phone,
            service=service, date=date, message=message
        )
        db.session.add(new_appt)
        db.session.commit()

        # send email asynchronously
        msg = Message(
            "New Appointment Request",
            sender="rodrigogf825@gmail.com",
            recipients=["rodrigogf825@gmail.com"]
        )
        msg.body = f"""
New Appointment Request

Name: {name}
Email: {email}
Phone: {phone}
Service: {service}
Date: {date}

Message:
{message}
"""
        Thread(target=send_async_email, args=(app, msg)).start()

        return "Appointment Submitted!"

    return render_template("book.html")

# Run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ensures table exists
    app.run(debug=True)