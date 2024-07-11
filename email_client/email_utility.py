import email
import imaplib
import os
from datetime import datetime
from email.header import decode_header
from email.utils import parsedate_to_datetime, parseaddr

from dotenv import load_dotenv

from . import models

load_dotenv()


def connect_email():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(os.getenv('EMAIL_USERNAME'), os.getenv('EMAIL_PASSWORD'))
    return mail


def check_email():
    mail = connect_email()
    mail.select("inbox")
    now = datetime.now().strftime("%d-%b-%Y")

    status, messages = mail.search(None, f'(UNSEEN SINCE "{now}")')
    # status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()

    if email_ids:
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = decode_header(msg['Subject'])[0][0]
                    from_name, from_email = parseaddr(msg.get('From'))
                    date_str = msg.get('Date')
                    sent_at = parsedate_to_datetime(date_str)
                    message_id = msg.get('Message-ID')
                    if isinstance(email_subject, bytes):
                        email_subject = email_subject.decode()

                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                email_body = part.get_payload(decode=True).decode()
                                break
                    else:
                        email_body = msg.get_payload(decode=True).decode()

                    if not models.Email.objects.filter(message_id=message_id).exists():
                        # Save the email to the database
                        email_obj = models.Email(
                            from_name=from_name,
                            from_email=from_email,
                            subject=email_subject,
                            body=email_body,
                            sent_at=sent_at,
                            status='received',
                            message_id=message_id
                        )
                        email_obj.save()

    mail.logout()
