import smtplib
import ssl
from f import *
import keyboard


def send_mail(message):

    sender_email = "yttube35@gmail.com"
    # receiver_email = "whyiswhen@gmail.com"
    receiver_email = "easylist@protonmail.com"
    # receiver_email = "singhalchirag@protonmail.com"

    password = "imhappyy"

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)

        print("Sending email to: ", receiver_email)

        server.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully")


def mi_to_mel(site_url, site_domain, image_url):

    subject = f"Report advertisement on {site_domain}"

    message = f"""Hi,

    Issue_url: {site_url}
    
    Issue : advertisement
    
    Screenshot:  {image_url} 

    System configuration: https://user-images.githubusercontent.com/76880977/126797496-0434116b-fc94-42c9-8139-fba02a985cf2.png

    Please resolve the issue as soon as possible.
    
    Thanks,
    """

    message = "Subject: {}\n\n{}".format(subject, message)

    print("message: ", message)

    send_mail(message)


def mi_to_send_mail_to_el():

    site_url, site_domain = ss_url_domain_closetab()

    image_url = check_if_image_uploaded_and_return_url()

    mi_to_mel(site_url, site_domain, image_url)


if __name__ == "__main__":

    # send_mail("hi")

    while True:

        if keyboard.is_pressed("ctrl + q"):

            mi_to_send_mail_to_el()

        else:
            sleep(0.1)
