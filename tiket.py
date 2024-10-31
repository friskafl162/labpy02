# harga tiket
harga_reguler = 50000
harga_vip = 100000

# input tipe tiket
tipe_tiket = input ("masukan tipe tiket (reguler/vip): ").lower()

# input status member
status_member = input("apakah anda memiliki kartu member? (ya/tidak): ").lower()

# menentukan harga tiket berdasarkan tipe tiket dan member
if tipe_tiket == "reguler":
    harga_tiket = harga_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_vip
else:
    print("tipe tiket tidak valid.")
    exit()

# menghitung harga dengan diskon jika pengguna adalah member
if status_member== "ya":
    total_harga = harga_tiket * 0.8 #diskon 20%
else:
    total_harga = harga_tiket

# output total harga yang harus dibayar 
print("total harga yang harus dibayar: Rp", int(total_harga))



     

