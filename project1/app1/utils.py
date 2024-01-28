from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client(email):
    subject="Sign-Up confirmation"
    message="This is an auto generated email.Pls don't reply."
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,from_email,recipient_list)