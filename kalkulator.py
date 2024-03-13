"""Hello selamat Pagi/Siang/Malam pengguna program"""

import sys,time
import pyfiglet

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

result = pyfiglet.figlet_format("Kalkulator Sederhana")
print(53*"=")
autoketik(result)

print(53*"=")
print("            Program ini dibuat oleh Fadil           ")
print(53*"="+ "\n")

msg = input("Masukan nama kamu:")
if msg == "orang":
	print("Enjoy my program")
	print("Jangan lupa bintangnya di github ya")
elif msg == "fadil":
	print("Kamu adalah developer dari program ini")
elif msg == "manusia":
    print("Jelas kamu manusia karena robot tidak bisa run program ini")
elif msg == "kontol":
    print("Jangan ngomong kotor wehh")
elif msg == "Pesan Moral":
    print("Belajarlah jangan menjadi yang TERBAIK dari sekian banyak orang,") 
    print("Tetapi jadilah orang yang bermental BAIK dari sekian banyak orang.")
else:
    print("Selamat datang di program Gwehh")
print("Akhir dari sebuah program")

print(53*"=")
print("              Mulai Kalkulator Sederhana             ")
print(53*"="+ "\n")

num1 = float(input("Masukan angka pertama ="))
operasi = input(" operasi (+,-,x,/,%)  =")
num2 = float(input("Masukan angka kedua   ="))
print()

if operasi  == "+":
    print("Hasil dari",num1,"+",num2,"adalah",round(num1+num2,2))
elif operasi  == "-":
    print("Hasil dari",num1,"-",num2,"adalah",round(num1-num2,2))
elif operasi  == "x":
    print("Hasil dari",num1,"x",num2,"adalah",round(num1*num2,2))
elif operasi  == "/":
    print("Hasil dari",num1,"/",num2,"adalah",round(num1/num2,2))
elif operasi  == "%":
    print("Hasil dari",num1,"%",num2,"adalah",round(num1%num2,2))
else:
    print("Maaf pilihan operasi tidak tersedia.")
print(53*"=")
print("             Terimakasih telah menggunakan    ") 
print("                     program ini              ")
print(53*"="+ "\n")
