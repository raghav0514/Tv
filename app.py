from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import config

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email configuration
app.config.update(
    MAIL_SERVER='sandbox.smtp.mailtrap.io',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=config.EMAIL,
    MAIL_PASSWORD=config.PASSWORD
)
mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-mail", methods=["POST"])
def send_mail():
    try:
        name = request.form["name"]
        email = request.form["email"]
        Phone_no = request.form["phone no"]
        Address = request.form["Address"]

        msg = Message(
            subject=f"TV Repair Request from {name}",
            sender=config.EMAIL,
            recipients=[config.EMAIL],
            body=f"Name: {name}\nEmail: {email}\nPhone NO:{Phone_no}\nAddress:\n{Address}"
        )
        mail.send(msg)
        flash("Your request has been sent successfully!", "success")
        return redirect(url_for("thank_you"))
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "danger")
        return redirect(url_for("error"))

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)