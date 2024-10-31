angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Pilih operasi aritmatika:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
operator = input("Masukkan pilihan operasi (+, -, *, /): ")

if operator == '+':
    hasil = angka1 + angka2
    print("Hasil dari penjumlahan:", hasil)
elif operator == '-':
    hasil = angka1 - angka2
    print("Hasil dari pengurangan:", hasil)
elif operator == '*':
    hasil = angka1 * angka2
    print("Hasil dari perkalian:", hasil)
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasil dari pembagian:", hasil)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Operator tidak valid. Silakan pilih (+, -, *, /).")