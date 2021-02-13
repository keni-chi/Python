# 二段階認証を有効化
# アプリパスワードを生成

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

fromAddress = 'xxx@gmail.com'
password = 'パスワード'
toAddress = 'xxx@gmail.com'

subject = '件名test'
bodyText = '本文test'

# SMTPサーバに接続
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
smtpobj.login(fromAddress, password)

# メール作成
msg = MIMEText(bodyText)
msg['Subject'] = subject
msg['From'] = fromAddress
msg['To'] = toAddress
msg['Date'] = formatdate()

# 作成したメールを送信
smtpobj.send_message(msg)
smtpobj.close()
