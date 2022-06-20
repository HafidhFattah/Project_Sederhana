masa_kerja= int(input("masukkan masa kerja:"))
umur= int(input("masukkan umur:"))

if masa_kerja >= 5 and umur >50:
    # aksi untuk bonus
    print("anda mendapat bonus 20%")
 elif masa_kerja >= 5:
     #aksi masa kerja >= 50
     print("anda dapat bonus 10%")
 else:
     # kurang dari 5 tahun
     print("Gaji kamu saya potong")
