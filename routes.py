# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail, Message

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
# db = SQLAlchemy(app)

# # Appointment model here...
# class Appointment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(120))
#     phone = db.Column(db.String(20))
#     service = db.Column(db.String(100))
#     date = db.Column(db.String(50))
#     message = db.Column(db.Text)

# # Mail setup here...
# mail = Mail(app)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     return render_template("index.html")

# @app.route("/gallery")
# def gallery():
#     return render_template("gallery.html")

# @app.route("/contact")
# def contact_page():
#     return render_template("contact.html")

# @app.route("/FreeEstimate")
# def free_estimate():
#     return render_template("contact.html")

# @app.route("/uncle")
# def uncle():
#     return render_template("uncle.html")

# @app.route("/book", methods=["GET", "POST"])
# def book():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]
#         phone = request.form["phone"]
#         service = request.form["service"]
#         date = request.form["date"]
#         message = request.form["message"]

#         # Save to database
#         new_appt = Appointment(name=name, email=email, phone=phone,
#                                service=service, date=date, message=message)
#         db.session.add(new_appt)
#         db.session.commit()

#         # Send email
#         msg = Message("New Appointment Request",
#                       sender="Luismpaez23@gmail.com",
#                       recipients=["Luismpaez23@gmail.com"])
#         msg.body = f"""
# New Appointment Request

# Name: {name}
# Email: {email}
# Phone: {phone}
# Service: {service}
# Date: {date}

# Message:
# {message}
# """
#         mail.send(msg)
#         return "Appointment Submitted!"

#     # return render_template("book.html")