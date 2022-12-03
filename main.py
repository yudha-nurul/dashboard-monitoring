"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import gempaterkini

if __name__ == '__main__':
    print('aplikasi utama')
    print('-' * 40)
    result = gempaterkini.ekstraksi_data()
    if result is None:
        print('program berhenti')
    else:
        gempaterkini.tampilkan_data(result)
    print('-' * 40)
