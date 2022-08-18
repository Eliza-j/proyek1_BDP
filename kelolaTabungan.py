import csv
import os
from os.path import exists
from datetime import datetime

class Savings:
    def __init__(self):
        self.entries = []
        self.total = 0

    def dataOpen(self, fileName):
        if exists(fileName):
            csv_file = open(fileName,'r')
            csv_reader = csv.reader(csv_file, delimiter=',')
            
            for row in csv_reader:
                self.entries.append(row)
        else:
             csv_file = open(fileName,'w')

    def calculateTotal(self):
        for entry in self.entries:
            self.total += int(entry[1])
        return self.total

    def dataInput(self, fileName):
        try:
            amounts = int(input("Masukkan jumlah: "))
            details = input("Masukkan keterangan: ")
            if amounts + self.total >= 0:
                self.__dataWrite(fileName, amounts, details)
            else:
                print("Tidak cukup uang!!!!\n")
            
        except ValueError:
            print("Tolong memasukkan data yang benar")
        
    
    def __dataWrite(self, fileName, amounts, details):
        csv_file = open(fileName,'a',newline='')
        now = datetime.now()
        try:
            tes_writer = csv.writer(csv_file)
            tes_writer.writerow([now.strftime("%d/%m/%Y %H:%M:%S"), amounts, details])
        except:
            print("Something's Wrong")

    def dataTransaksi(self):
        self.calculateTotal()
        print("********** PENGELOLA TABUNGAN **********")
        print("\nTotal Tabungan: ", self.calculateTotal())
        print("")
        print("5 transaksi terakhir: ")


        print("{:<25} {:<15} {:<10}".format('Tanggal','Jumlah','Keterangan'))

        for entry in reversed(saving.entries[-5:]):
            date, amount, details = entry
            print ("{:<25} {:<15} {:<10}".format(date, amount, details))

        while True:
            back = input("Kembali? (ya)")
            if back == "ya":
                Menu()
            else:
                print("Invalid input")
            continue
            

    def showAll(self):
        pass

fileName = 'savings'

#while True:
saving = Savings()
#saving.dataOpen(fileName)

def Menu():
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    clear()
    #saving = Savings()
    saving.dataOpen(fileName)

    print("--------------------------------------------------------")
    print("""Menu:
    1. Catat transaksi baru
    2. Tampilkan seluruh transaksi
    3. Keluar
    """)

    #selectedMenu = input('Pilih menu: ')
    while True:
        selectedMenu = input('Pilih menu: ')
        if selectedMenu == '1':
            saving.dataInput(fileName)
            #adalagi = input("Ada lagi? (ya/tidak)")
            while True:
                adalagi = input("Ada lagi? (ya/tidak)")
                if adalagi == "ya":
                    Menu()
                elif adalagi == "tidak":
                    exit()
                else:
                    print("Invalid input")
                continue
        elif selectedMenu == '2':
            saving.dataTransaksi()
            #continue
        elif selectedMenu == '3':
            exit()
        else:
            print("Invalid input \n")
        continue

Menu()






# csv_file = open('tes.txt','a',newline='')
# tes_writer = csv.writer(csv_file)
# tes_writer.writerow([-50000, '02-02-3039', 'mouse'])
# tes_writer.writerow([70000, '19-29-2023', 'jajan'])
# csv_reader = csv.reader(csv_file, delimiter=',')
# line_count = 0
# for row in csv_reader:
#     print(row)
# print(f'Processed {line_count} lines.')


# from datetime import datetime

# # datetime object containing current date and time
# now = datetime.now()
 
# print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)	
