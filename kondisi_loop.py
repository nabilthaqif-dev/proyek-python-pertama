# kondisi_loop.py

# 1. KONDISI (IF / ELIF / ELSE)
nilai_ujian = 55

print(f"Nilai ujian kamu: {nilai_ujian}")
if nilai_ujian >= 90:
    print("Grade: A (Sangat Baik)")
elif nilai_ujian >= 75:
    print("Grade: B (Baik)")
elif nilai_ujian >= 60:
    print("Grade: C (Cukup)")
else:
    print("Grade: D (Perlu Belajar Lagi)")

print("-" * 20) # Mencetak garis pemisah

# 2. LOOPING (FOR)
# Mencetak angka 1-5
print("Mencetak angka 1-10:")
for angka in range(1, 11):
    print(f"Angka ke-{angka}")

print("-" * 20)

# 3. LOOPING (WHILE)
# Hitung mundur (countdown)
print("Hitung mundur:")
hitung = 3
while hitung > 0:
    print(hitung)
    hitung -= 1 # Ini sama dengan hitung = hitung - 1
print("Meluncur! 🚀")

print("-" * 20)

# 1. Ambil input pertama dan tukar kepada integer (int)
tebakan = int(input("Tebak nombor: "))
salah = "Tebak lagi!"

# 2. Gelung akan berjalan selagi tebakan BUKAN 7 
while tebakan != 7:
    print(salah)
    # 3. Minta pengguna masukkan tebakan baharu di dalam gelung
    tebakan = int(input("Tebak nombor: "))

# 4. Mesej ini akan keluar jika tebakan ADALAH 7
print("Tahniah! Tebakan anda betul.")
    
    
