"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
# import gempaterkini
import latihan_gempaterkini
if __name__ == '__main__':
    print('aplikasi utama')
    # result = gempaterkini.ekstraksi_data()
    # gempaterkini.tampilkan_data(result)
    result = latihan_gempaterkini.ekstraksi_data()
    latihan_gempaterkini.tampilkan_data(result)
