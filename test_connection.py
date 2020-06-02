from smtplib import SMTP
with SMTP("smtp.domain") as smtp:
    smtp.noop()
