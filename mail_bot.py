def GmailBot():
    # gets libraries for code
    import smtplib
    from email.message import EmailMessage

    mail_address = input('Enter Email Address Here --> ') # mail address for bot account
    mail_password = input('Enter Email Password Here --> ') # mail password for bot account
    reciver = input('Who are you emailing? ') # gets email address for renter
    subject = input('What is the Subject of the Email? ') # gets email subject
    body = input('What is the body of the emai? ') # gets email body (main text)

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = mail_address
    msg['To'] = reciver
    msg.set_content(body)





    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(mail_address, mail_password)

        smtp.send_message(msg)
        print('Email Sent')
