class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, nama, nim, akt):
        self.nama = nama
        self.nim = nim
        self.akt = akt
        Employee.empCount += 1

    def tampilkan_jumlah(self):
        print("Total Mahasiswa %d" % Employee.empCount)

    def tampilkan_data(self):
        print(f'\nNama Mahasiswa \t: {self.nama}\nNIM \t\t: {self.nim}\nAngkatan \t: {self.akt}')



nm = str(input("Masukkan nama : "))
ni = str(input("Masukkan NIM : "))
ak = str(input("Masukkan angkatan : "))

emp = Employee(nm, ni, ak)
emp.tampilkan_data()
print("\nTotal Mahasiswa %d" % Employee.empCount)