from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


# Substituir valores das variaveis no e-mail.
with open('modulo_5/template.html', 'r') as arquivo:
    # ler arquivo
    template = Template(arquivo.read())
    # data atual formatada
    data_atual = datetime.now().strftime('%d/%m/%Y')
    # substituir valores
    corpo_msg = template.substitute(nome= 'William Crystian', data= data_atual)
    
msg = MIMEMultipart()

# de
msg['from'] = 'William Crystian Aniceto'
# para
msg['to'] = '@gmail.com'
# assunto
msg['subject'] = 'Atenção: este é um e-mail de testes.'

# passando para MIMEText o e-mail em html
corpo = MIMEText(corpo_msg, 'html')

#texto a ser enviado
msg.attach(corpo)

#enviando uma imagem em anexo
#with open('imagem.jpg', 'rb') as img:
#    img = MIMEImage(img.read())
#    msg.attach(img)

# enviar o e-mail
with smtplib.SMTP(host='smtp-relay.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        # e-mail e login de quem ta enviando
        smtp.login('@gmail.com.br', 'senha')
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não foi possivel enviar.')
        print('Erro:', e)