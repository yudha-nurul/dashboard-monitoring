
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
    hasilnya = dict()
    hasilnya['tanggal'] = '10 November 2022'
    hasilnya['waktu'] = '12:56:30 WIB'
    hasilnya['magnitudo'] = '4.9'
    hasilnya['kedalaman'] = '10 km'
    hasilnya['lokasi'] = {'LU': 4.28, 'BT': 96.72}
    hasilnya['pusat gempa'] = 'Pusat gempa berada di darat 40 km BaratDaya Takengon'
    hasilnya['dirasakan'] = 'Dirasakan (Skala MMI): III Nagan Raya, III Benermeriah, I-II Pidie, I-II Lhokseumawe'

    return hasilnya


def tampilkan_data(hasilnya):
    print('gempa terakhir berdasarkan BMKG:')
    print(f"tanggal {hasilnya['tanggal']}")
    print(f"waktu {hasilnya['waktu']}")
    print(f"magnitudo {hasilnya['magnitudo']}")
    print(f"kedalaman {hasilnya['kedalaman']}")
    print('lokasi:')
    print(f"    LU= {hasilnya['lokasi']['LU']}")
    print(f"    BT= {hasilnya['lokasi']['BT']}")
    print(hasilnya['pusat gempa'])
    print(hasilnya['dirasakan'])
