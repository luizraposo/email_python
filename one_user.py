from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


meu_email = ''
minha_senha = ''

with open('corpo.html', 'r') as html:
    template = Template(html.read())
    corpo_msg = template.substitute()

recipients = '#CLIENTE'
msg = MIMEMultipart()
msg['from'] = ''
msg['to'] = recipients  #CLIENTE
msg['subject'] = 'Assunto'

corpo = MIMEText('')
msg.attach(corpo)

with smtplib.SMTP('') as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)

        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
