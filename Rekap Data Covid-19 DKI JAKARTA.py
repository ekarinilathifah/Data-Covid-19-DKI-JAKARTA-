#library
import csv
import os
import functools
from itertools import chain

#variabel
database = []
kecamatan = []
odp = []
proses_pemantauan = []
selesai_pemantauan = []
pdp = []
masih_dirawat = []
pulang_dan_sehat = []
positif = []
dirawat = []
sembuh = []
meninggal = []
isolasi_mandiri = []
database = []

#membuka vile csv
with open('D:\SEMESTER 3\PEMROGRAMAN FUNGSIONAL\TUBES\data1.csv') as csvfile:
    readCSV = csv.DictReader(csvfile) #menggunakan directory
    #menggunakan perulangan dimana variabel row berisi
    #sebuah list dari setiap data di csv
    for row in readCSV:
        #menuliskan dalam database
        #atau menambahkan data dari csv ke database
        database.append(row)
        
    #menggunakan perulangan dimana variabel data
    # berisi list dari database

for data in database:
    kecamatan1 = str(data['kecamatan'])
    odp1 = int(data['odp'])
    prosespemantauan1 = int(data['proses_pemantauan'])
    selesaipemantauan1 = int(data['selesai_pemantauan'])
    pdp1 = int(data['pdp'])
    masihdirawat1 = int(data['masih_dirawat'])
    pulangdansehat1 = int(data['pulang_dan_sehat'])
    positif1 = int(data['positif'])
    dirawat1 = int(data['dirawat'])
    sembuh1 = int(data['sembuh'])
    meninggal1 = int(data['meninggal'])
    isolasimandiri1 = int(data['isolasi_mandiri'])
    
    kecamatan.append(kecamatan1)
    odp.append(odp1)
    proses_pemantauan.append(prosespemantauan1)
    selesai_pemantauan.append(selesaipemantauan1)
    pdp.append(pdp1)
    masih_dirawat.append(masihdirawat1)
    pulang_dan_sehat.append(pulangdansehat1)
    positif.append(positif1)
    dirawat.append(dirawat1)
    sembuh.append(sembuh1)
    meninggal.append(meninggal1)
    isolasi_mandiri.append(isolasimandiri1)
    
#menu
def menu():
    print("\n")
    print("------------ KELOMPOK 13 ------------")
    print(" 1. Ekarini Lathifah     20102096    ")
    print(" 2. Putri Pusparini      20102127    ")
    print(" 3. Hesny Umayasyah      20102168    ")
    print("-------------------------------------")
    print("**************S1IF08M****************")
    print("\n")
    print("========================================")
    print("------ CASES COVID-19 DKI JAKARTA ------")
    print(" 1. Tampilkan data covid-19             ")
    print(" 2. Total kasus data covid-19           ")
    print(" 3. Filter huruf kecamatan              ")
    print(" 4. Urutkan sesuai abjad                ")
    print(" 5. Huruf kecil                         ")
    print(" 6. Search data covid-19                ")
    print(" 0. Exit                                ")
    print("========================================")
    print("\n")
    print("_____________ TERIMA KASIH _____________")
    print("\n")
    
#menampilkan data
def tampil_data():
    for data in database:
        kecamatan = str(data['kecamatan'])
        odp = int(data['odp'])
        proses_pemantauan = int(data['proses_pemantauan'])
        selesai_pemantauan = int(data['selesai_pemantauan'])
        pdp = int(data['pdp'])
        masih_dirawat = int(data['masih_dirawat'])
        pulang_dan_sehat = int(data['pulang_dan_sehat'])
        positif = int(data['positif'])
        dirawat = int(data['dirawat'])
        sembuh = int(data['sembuh'])
        meninggal = int(data['meninggal'])
        isolasi_mandiri = int(data['isolasi_mandiri']) 
        print("==============================================")
        print("\n")
        print(f"Kecamatan\t\t: ",kecamatan)
        print(f"ODP\t\t\t: ",odp)
        print(f"Proses Pemantauan\t: ",proses_pemantauan)
        print(f"Selesai Pemantauan\t: ",selesai_pemantauan)
        print(f"PDP\t\t\t: ",pdp)
        print(f"Masih dirawat\t\t: ",masih_dirawat)
        print(f"Pulang dan sehat\t: ",pulang_dan_sehat)
        print(f"Positif\t\t\t: ",positif)
        print(f"Dirawat\t\t\t: ",dirawat)
        print(f"Sembuh\t\t\t: ",sembuh)
        print(f"Meninggal\t\t: ",meninggal)
        print(f"Isolasi Mandiri\t\t: ",isolasi_mandiri, "\n")
        print("\n")
        print("================================================")
    
    os.system('pause')
    os.system('cls')

#menghitung total casus 
def jumlah_covid19():
    total_odp = []
    total_prosespemantauan = []
    total_selesaipemantauan = []
    total_pdp = []
    total_masihdirawat = []
    total_pulangdansehat = []
    total_positif = []
    total_dirawat = []
    total_sembuh = []
    total_meninggal =[]
    total_isolasimandiri = []
    
    a = functools.reduce(lambda n,m: n+m, odp)
    b = functools.reduce(lambda o,p: o+p, proses_pemantauan)
    c = functools.reduce(lambda q,r: q+r, selesai_pemantauan)
    d = functools.reduce(lambda s,t: s+t, pdp)
    e = functools.reduce(lambda u,v: u+v, masih_dirawat)
    f = functools.reduce(lambda w,x: w+x, pulang_dan_sehat)
    g = functools.reduce(lambda y,z: y+z, positif)
    h = functools.reduce(lambda l,a: l+a, dirawat)
    i = functools.reduce(lambda b,c: b+c, sembuh)
    j = functools.reduce(lambda d,e: d+e, meninggal)
    k = functools.reduce(lambda f,g: f+g, isolasi_mandiri)
    
    total_odp.append(a)
    total_prosespemantauan.append(b)
    total_selesaipemantauan.append(c)
    total_pdp.append(d)
    total_masihdirawat.append(e)
    total_pulangdansehat.append(f)
    total_positif.append(g)
    total_dirawat.append(h)
    total_sembuh.append(i)
    total_meninggal.append(j)
    total_isolasimandiri.append(k)
    
    res = sum(chain(odp, proses_pemantauan, selesai_pemantauan, pdp, masih_dirawat, pulang_dan_sehat, positif, dirawat, sembuh, meninggal, isolasi_mandiri)) / len(list(chain(odp, proses_pemantauan, selesai_pemantauan, pdp, masih_dirawat, pulang_dan_sehat, positif, dirawat, sembuh, meninggal, isolasi_mandiri)))
    
    print("================= DATA ===============")
    print(" Total odp                   : ", a)
    print(" Total proses pemantauan     : ", b)
    print(" Total selesai pemantauan    : ", c)
    print(" Total pdp                   : ", d)
    print(" Total masih dirawat         : ", e)
    print(" Total pulang dan sehat      : ", f)
    print(" Total positif               : ", g)
    print(" Total dirawat               : ", h)
    print(" Total sembuh                : ", i)
    print(" Total meninggal             : ", j)
    print(" Total isolasi mandiri       : ", k)
    print(" Rasio kasus covid-19        : ", list(map(lambda a,b,c,d,e,f,g,h,i,j,k: a/b/c/d/e/f/g/h/i/j/k*100, total_odp, total_prosespemantauan, total_selesaipemantauan, total_pdp, total_masihdirawat, total_pulangdansehat, total_positif, total_dirawat, total_sembuh, total_meninggal, total_isolasimandiri)))
    print("=======================================")
    print("\n")
    
def duplicates(lst, item):
    return[i for i, x in enumerate(lst) if x== item]

#cari data
def cari():
    kecamatan = input("Cari berdasarkan kecamatan : ")
    
    data_found = []
    
    #mencari
    indeks = 0
    for data in database:
        if (data['kecamatan'] == kecamatan):
            data_found = database[indeks]
        
        indeks = indeks+ 1
    
    if len(data_found) > 0:
        print("\n")
        print("DATA DITEMUKAN ")
        print(f"Kecamatan           : {data_found['kecamatan']}")
        print(f"ODP                 : {data_found['odp']}")
        print(f"Proses pemantauan   : {data_found['proses_pemantauan']}")
        print(f"Selesai pemantauan  : {data_found['selesai_pemantauan']}")
        print(f"PDP                 : {data_found['pdp']}")
        print(f"Masih dirawat       : {data_found['masih_dirawat']}")
        print(f"Pulang dan sehat    : {data_found['pulang_dan_sehat']}")
        print(f"Positif             : {data_found['positif']}")
        print(f"Dirawat             : {data_found['dirawat']}")
        print(f"Sembuh              : {data_found['sembuh']}")
        print(f"Meninggal           : {data_found['meninggal']}")
        print(f"Isolasi mandiri     : {data_found['isolasi_mandiri']}")
    else :
        print(" Data tidak ditemukan ")
    
#mencari huruf vokal dari nama kecamatan
def filter_kecamatan():
    for data in database:
        kecamatan = str(data['kecamatan'])
        abjad = kecamatan
        def filter_vocal(abjad):
            vocal = ['A', 'I', 'U', 'E', 'O']
            if abjad in vocal:
                return True
            else:
                return False
        
        vocal_terfilter = filter(filter_vocal, kecamatan)
        print(kecamatan, 'Huruf vocal yang tersaring adalah: ')
        for vocal in vocal_terfilter:
            print(vocal)

#mengurutkan ejaan nama kecamatan
def sorted_list():
    for data in database:
        kecamatan = str(data['kecamatan'])
        print(kecamatan, '\n\n', '\t', sorted(kecamatan.lower()), '\n')

#mengubah nama kecamatan menjadi huruf kecil
def huruf_kecil():
    for data in database:
        kecamatan = str(data['kecamatan'])
        print(kecamatan, '\n', list(map(str.lower,kecamatan)))

#pilihan menu
jawab = True
while(jawab):
    menu()
    pilih_menu = input("Masukkan pilihan Anda: ")
    
    if (pilih_menu == "1"):
        tampil_data()
    elif(pilih_menu == "2"):
        jumlah_covid19()
    elif (pilih_menu == "3"):
        filter_kecamatan()
    elif (pilih_menu == "4"):
        sorted_list()
    elif (pilih_menu == "5"):
        huruf_kecil()
    elif (pilih_menu == "6"):
        cari()
    elif (pilih_menu == "0"):
        jawab = False  