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
    global tanggal, waktu, magnitudo, kedalaman, lu, bt, pusat, dirasakan
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        print('the content cannot displayed')
        return None

    # print(content.status_code)
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        tanggal_waktu = soup.find('span', {'class': 'waktu'})
        tanggal_waktu = tanggal_waktu.text
        tanggal_waktu = tanggal_waktu.split(', ')
        tanggal = tanggal_waktu[0]
        waktu = tanggal_waktu[1]

        list_result = soup.find('div', {'class': "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        list_result = list_result.text
        list_result = list_result.split('\n')
        magnitudo = None
        kedalaman = None
        lu = None
        bt = None
        pusat = None
        dirasakan = None

        magnitudo = list_result[3]
        kedalaman = list_result[4]
        alu = list_result[5]
        alu = alu.split('-')
        lu = alu[0]
        bt = alu[1]
        pusat = list_result[6]
        dirasakan = lu[7]

    hasilnya = dict()
    hasilnya['tanggal'] = tanggal
    hasilnya['waktu'] = waktu
    hasilnya['magnitudo'] = magnitudo
    hasilnya['kedalaman'] = kedalaman
    hasilnya['lokasi'] = {'lu': lu, 'bt': bt}
    hasilnya['pusat gempa'] = pusat
    hasilnya['dirasakan'] = dirasakan

    return hasilnya


def tampilkan_data(hasilnya):
    print('gempa terakhir berdasarkan BMKG:')
    print(f"tanggal {hasilnya['tanggal']}")
    print(f"waktu {hasilnya['waktu']}")
    print(f"magnitudo {hasilnya['magnitudo']}")
    print(f"kedalaman {hasilnya['kedalaman']}")
    print('lokasi:')
    print(f"    LU= {hasilnya['lokasi']['lu']}")
    print(f"    LS= {hasilnya['lokasi']['bt']}")
    print(hasilnya['pusat gempa'])
    print(hasilnya['dirasakan'])
