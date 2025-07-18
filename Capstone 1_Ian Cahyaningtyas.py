from datetime import datetime

# Data guru
data_guru = [
    {
        'nama':'Dina Mariana',
        'tanggal_lahir': datetime(1980, 10, 12),
        'jenis_kelamin':'perempuan',
        'usia': 44,
        'tingkat_stress':'rendah',
        'kepuasan_kerja':'sedang',
        'beban_kerja':'rendah',
        'warna_kepribadian':'kuning'
    }, 
    {
        'nama':'Winston Liem',
        'tanggal_lahir': datetime(1985, 4, 9),
        'jenis_kelamin':'laki-laki',
        'usia': 40,
        'tingkat_stress':'tinggi',
        'kepuasan_kerja':'sedang',
        'beban_kerja':'rendah',
        'warna_kepribadian':'merah'
    },
    {
        'nama':'Mira Kartika',
        'tanggal_lahir': datetime(1990, 7, 4),
        'jenis_kelamin':'perempuan',
        'usia': 35,
        'tingkat_stress':'rendah',
        'kepuasan_kerja':'sedang',
        'beban_kerja':'tinggi',
        'warna_kepribadian':'hijau'
    },
    {
        'nama':'Tono Prasetyo',
        'tanggal_lahir': datetime(1995, 6, 28),
        'jenis_kelamin':'laki-laki',
        'usia': 30,
        'tingkat_stress':'tinggi',
        'kepuasan_kerja':'rendah',
        'beban_kerja':'sedang',
        'warna_kepribadian':'biru'
    },
    {
        'nama':'Valerie Susanto',
        'tanggal_lahir': datetime(1988, 3, 6),
        'jenis_kelamin':'perempuan',
        'usia': 37,
        'tingkat_stress':'tinggi',
        'kepuasan_kerja':'sedang',
        'beban_kerja':'sedang',
        'warna_kepribadian':'merah'
    },
    {
        'nama':'Gita Gunawan',
        'tanggal_lahir': datetime(1996, 7, 7),
        'jenis_kelamin':'perempuan',
        'usia': 29,
        'tingkat_stress':'tinggi',
        'kepuasan_kerja':'sedang',
        'beban_kerja':'tinggi',
        'warna_kepribadian':'biru'
    },
    {
        'nama':'Kiki Anggraini',
        'tanggal_lahir': datetime(1994, 1, 30),
        'jenis_kelamin':'perempuan',
        'usia': 31,
        'masa_kerja': 6,
        'tingkat_stress':'tinggi',
        'kepuasan_kerja':'rendah',
        'beban_kerja':'tinggi',
        'warna_kepribadian':'kuning'
    },
    {
        'nama':'Sari Pratama',
        'tanggal_lahir': datetime(1991, 8, 17),
        'jenis_kelamin':'perempuan',
        'usia': 33,
        'tingkat_stress':'rendah',
        'kepuasan_kerja':'tinggi',
        'beban_kerja':'sedang',
        'warna_kepribadian':'merah'
    }
]

def id_guru(guru):
    return f"{guru['nama'].upper().replace(' ', '_')}_{guru['tanggal_lahir'].strftime('%Y%m%d')}"

def tingkat_burnout(guru):
    tingkat_stress = guru['tingkat_stress']
    beban_kerja = guru['beban_kerja']
    kepuasan_kerja = guru['kepuasan_kerja']

    if tingkat_stress == 'tinggi' and beban_kerja == 'tinggi' and kepuasan_kerja in ['rendah', 'sedang']:
        return 'tinggi'
    elif tingkat_stress == 'tinggi' and beban_kerja == 'sedang' and kepuasan_kerja == 'rendah':
        return 'tinggi'
    elif tingkat_stress in ['sedang', 'tinggi'] and beban_kerja == 'tinggi' and kepuasan_kerja == 'rendah':
        return 'tinggi'
    elif tingkat_stress == 'rendah' and beban_kerja == 'rendah' and kepuasan_kerja == 'tinggi':
        return 'rendah'
    else:
        return 'sedang'
    
def menambah_data_guru():
    nama = input('Masukkan Nama: ')
    tanggal_lahir = datetime.strptime(input("Masukkan Tanggal Lahir (YYYY-MM-DD): "), "%Y-%m-%d")
    jenis_kelamin = input('Masukkan Jenis Kelamin: ')
    usia = int(input('Masukkan Usia: '))
    warna_kepribadian = input('Masukkan Warna Kepribadian: ')
    tingkat_stress = input('Masukkan Tingkat Stress (rendah/sedang/tinggi): ')
    kepuasan_kerja = input('Masukkan Kepuasan Kerja (rendah/sedang/tinggi): ')
    beban_kerja = input('Masukkan Beban Kerja (rendah/sedang/tinggi): ')
    
    data_guru.append({
        'nama': nama,
        'tanggal_lahir': tanggal_lahir,
        'jenis_kelamin': jenis_kelamin,
        'usia': usia,
        'tingkat_stress': tingkat_stress,
        'kepuasan_kerja': kepuasan_kerja,
        'beban_kerja': beban_kerja,
        'warna_kepribadian': warna_kepribadian
    })
    print("✅ Data Guru berhasil ditambahkan.\n")

from prettytable import PrettyTable
def menampilkan_data_demografi():
    print('\n📊 Data Demografi Guru')
    print('=' * 110)
    tabel = PrettyTable()
    tabel.field_names = ["Index", "ID Guru", "Nama", "Tanggal Lahir", "Jenis Kelamin", "Usia", "Warna Kepribadian"]
    # print('=' * 110)
    for i, guru in enumerate(data_guru):
        tabel.add_row([
            i,
            id_guru(guru),
            guru['nama'],
            guru['tanggal_lahir'].strftime('%Y-%m-%d'),
            guru['jenis_kelamin'],
            guru['usia'],
            guru['warna_kepribadian']
        ])
        tabel.align = "l"
        print(tabel)
    print('=' * 110 + '\n')

def menampilkan_data_burnout():
    print("\n🔥 Data Burnout:\n")
    for guru in data_guru:
        print(f"{id_guru(guru)}: Burnout = {tingkat_burnout(guru)}")
    print()

def mengubah_data_demografi():
    menampilkan_data_demografi()
    index = int(input('Masukkan Index Guru yang ingin diubah: '))
    kolom = input('Masukkan kolom yang ingin diganti (nama/usia/tanggal_lahir/jenis_kelamin/warna_kepribadian): ')
    nilai = input('Masukkan nilai baru: ')
    if kolom == 'usia':
        nilai = int(nilai)
    elif kolom == 'tanggal_lahir':
        nilai = datetime.strptime(nilai, "%Y-%m-%d")
    data_guru[index][kolom] = nilai
    print("✅ Data demografi berhasil diubah.\n")

def mengubah_data_burnout():
    menampilkan_data_demografi()
    index = int(input("Masukkan index guru yang ingin ubah burnout-nya: "))
    kolom = input("Masukkan kolom burnout (tingkat_stress/beban_kerja/kepuasan_kerja): ")
    nilai = input("Masukkan nilai baru: ")
    data_guru[index][kolom] = nilai
    print("✅ Data burnout berhasil diubah.\n")

def menghapus_data_demografi():
    menampilkan_data_demografi()
    index = int(input("Masukkan index guru yang ingin dihapus dari data: "))
    del data_guru[index]
    print("✅ Data guru berhasil dihapus sepenuhnya.\n")

def menghapus_data_burnout():
    menampilkan_data_demografi()
    index = int(input("Masukkan index guru untuk menghapus data burnout-nya: "))
    if 0 <= index < len(data_guru):
        data_guru[index]['tingkat_stress'] = ''
        data_guru[index]['beban_kerja'] = ''
        data_guru[index]['kepuasan_kerja'] = ''
        print("✅ Data burnout berhasil dikosongkan.\n")
    else:
        print("❌ Index tidak valid.\n")

def menu_menampilkan_data():
    while True:
        pilihan = input('''
        === MENU TAMPILKAN DATA ===
        1. Menampilkan Data Demografi
        2. Menampilkan Data Burnout
        3. Kembali ke Menu Utama
        Pilih: ''')
        if pilihan == '1':
            menampilkan_data_demografi()
        elif pilihan == '2':
            menampilkan_data_burnout()
        elif pilihan == '3':
            break
        else:
            print("❌ Pilihan tidak valid.\n")

def menu_mengubah_data():
    while True:
        pilihan = input('''
        === MENU UBAH DATA ===
        1. Mengubah Data Demografi
        2. Mengubah Data Burnout
        3. Kembali ke Menu Utama
        Pilih: ''')
        if pilihan == '1':
            mengubah_data_demografi()
        elif pilihan == '2':
            mengubah_data_burnout()
        elif pilihan == '3':
            break
        else:
            print("❌ Pilihan tidak valid.\n")

def menu_menghapus_data():
    while True:
        pilihan = input('''
        === MENU HAPUS DATA ===
        1. Menghapus Data Guru (semua)
        2. Menghapus Data Burnout (kosongkan)
        3. Kembali ke Menu Utama
        Pilih: ''')
        if pilihan == '1':
            menghapus_data_demografi()
        elif pilihan == '2':
            menghapus_data_burnout()
        elif pilihan == '3':
            break
        else:
            print("❌ Pilihan tidak valid.\n")

def menu_utama():
    while True:
        pilihan = input('''
        ======= MENU UTAMA =======
        1. Menambah Data Guru
        2. Menampilkan Data Guru
        3. Mengganti Data Guru
        4. Menghapus Data Guru
        5. Keluar
        Pilih: ''')

        if pilihan == '1':
            menambah_data_guru()
        elif pilihan == '2':
            menu_menampilkan_data()
        elif pilihan == '3':
            menu_mengubah_data()
        elif pilihan == '4':
            menu_menghapus_data()
        elif pilihan == '5':
            print("👋 Terima kasih. Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid.\n")


menu_utama()
