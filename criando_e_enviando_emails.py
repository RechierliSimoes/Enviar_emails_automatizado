from smtplib import SMTP
import ssl
import email.message

msg = email.message.Message()
msg['Subject'] = 'assunto do email'

body = """
msg que será enviada, podendo ser editada pelos padrões html
"""

msg['From'] = 'email que ira enviar'
msg['To'] = 'email que ira receber'
password = 'senha do email'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)


context = ssl.create_default_context()
with SMTP('smtp.gmail.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(msg['From'], password)
    conexao.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
