"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import latihan_gempaterkini

if __name__ == '__main__':
    print('aplikasi utama')
    print('-' * 40)
    result = latihan_gempaterkini.ekstraksi_data()
    if result is None:
        print('program berhenti')
    else:
        latihan_gempaterkini.tampilkan_data(result)
    print('-' * 40)
