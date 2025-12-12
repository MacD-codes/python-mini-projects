import smtplib


def automatic_email():
    email = input("Enter your Email: ")
    sender_email = "mahekdalal14@gmail.com"
    subject = "Hello ji !!"

    full_msg = f"""From: {sender_email}
To: {email} 
Subject: {subject}

Usse jaane de Nagma,
Bhai usko jaane doon main? :0

Dekho,
Kaise pakad rahi hai woh aapko?
Waah Shampy Waahh !!!!

MacD-Codes:)"""

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(sender_email, "jxyl rgjx yuhz khtb")
    s.sendmail(sender_email, email, full_msg)
    print("Email Sent!")


automatic_email()
