import requests
from bs4 import BeautifulSoup
def ekstraksi_data():
    """
        Gempabumi Terkini
    Tanggal: 10 November 2022
    Waktu: 12:56:30 WIB
    Magnitudo: 4.9
    Kedalaman: 10 km
    Lokasi: 4.28 LU 96.72 BT
    Pusat Gempa: Pusat gempa berada di darat 40 km BaratDaya Takengon
    Dirasakan: Dirasakan (Skala MMI): III Nagan Raya, III Benermeriah, I-II Pidie, I-II Lhokseumawe
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        print('the content cannot displayed')
        return None
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.text)


def tampilkan_data():
    print('gempa terakhir berdasarkan BMKG:')
    print(f"tanggal {hasilnya['tanggal']}")
    print(f"waktu {hasilnya['waktu']}")
    print(f"magnitudo {hasilnya['magnitudo']}")
    print(f"kedalaman {hasilnya['kedalaman']}")
    print('lokasi:')
    print(f"    LU= {hasilnya['lokasi']['LS']}")
    print(f"    BT= {hasilnya['lokasi']['BT']}")
    print(hasilnya['pusat gempa'])
    print(hasilnya['dirasakan'])
