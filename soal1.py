import re
from datetime import datetime

teks = """Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02)."""

tanggal = re.findall(r'\d{4}-\d{2}-\d{2}', teks)
sekarang = datetime.now()

hasil = []
for tanggal_ in tanggal:
    tanggal_bro = datetime.strptime(tanggal_, '%Y-%m-%d')
    selisih = sekarang - tanggal_bro
    tanggal_hasil = tanggal_bro.strftime('%d-%m-%Y')
    hasil.append(f"{tanggal_bro} selisih {selisih.days} hari")

for item in hasil:
    print(item)