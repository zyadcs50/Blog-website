from flask import Flask, render_template, request, url_for
import requests

import smtplib
from email.message import EmailMessage

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=["GET", "POST"])
def form_entry():
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        my_email = "zezozoz131@gmail.com"
        my_pass = "ffah vcbw ffow fpuc"
        msg = EmailMessage()
        msg['subject'] = name
        msg['from'] = email
        msg['to'] = my_email
        msg.set_content(message)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # تشفير الاتصال
            server.login(my_email, my_pass)
            server.send_message(msg)
            
            # return "tthanks for contacting us"    
        return render_template("form_entry.html", name=name, email= email, phone = phone, message= message)
    
    


if __name__ == "__main__":
    app.run(debug=True, port=5001)
