import re

ptn = re.compile(r'[a-z0-9.!#$%&\'*+/=?^_{|}~-]+@[a-z0-9-]+(?:\.[a-z0-9-]+)+', re.IGNORECASE)
msg = 'お問い合わせはsupport@xample.comまで'
print(ptn.sub(r'<a href="\g<0>">\g<0></a>', msg))

