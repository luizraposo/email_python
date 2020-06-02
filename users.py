# envio de e-mail para múltiplos usuários com base num csv.

import smtplib
import csv,ssl


message =  """Subject: Assunto
corpo da menssagem
"""

from_address = ""


with smtplib.SMTP('smtp.domain') as smtp:
    try:
        with open("FILE.CSV") as file:
            reader = csv.reader(file)
            next(reader)

            for x, y, z, in reader:
                smtp.sendmail(
                    from_address,
                    email,
                    message.format(),

                )

        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
