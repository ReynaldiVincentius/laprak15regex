import re
import random
import string

teks = """Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari"""

email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', teks)

def password_acak(length = 8) :
    sandi = string.ascii_letters + string.digits
    hasil = ""
    for i in range(length) :
        hasil += random.choice(sandi)
    return hasil

for j in email :
    user = j.split('@')[0]
    password = password_acak()
    print(f"{j} username : {user}, password : {password}")