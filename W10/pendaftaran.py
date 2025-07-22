# SEBELUM REFACTORING
# ini hanya contoh kode untuk pendaftaran mahasiswa

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def register(self):
        if self.name == "":
            print("Nama tidak boleh kosong")
        elif self.age <= 0:
            print("Umur tidak valid")
        elif self.major == "":
            print("Jurusan tidak boleh kosong")
        else:
            print(f"{self.name} berhasil terdaftar di jurusan {self.major}")

# SETELAH REFACTORING
# Memisahkan logika pendaftaran ke dalam fungsi terpisah

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def register(self):
        # Memanggil validasi sebelum proses pendaftaran
        if not self.is_valid_name():
            print("Nama tidak boleh kosong")
        elif not self.is_valid_age():
            print("Umur tidak valid")
        elif not self.is_valid_major():
            print("Jurusan tidak boleh kosong")
        else:
            print(f"{self.name} berhasil terdaftar di jurusan {self.major}")

    # Refactoring: Ekstraksi metode validasi agar kode tidak duplikatif dan lebih bersih
    def is_valid_name(self):
        return self.name != ""

    def is_valid_age(self):
        return self.age > 0

    def is_valid_major(self):
        return self.major != ""
    
# Contoh penggunaan
if __name__ == "__main__": 
    student1 = Student("Alice", 20, "Computer Science")
    student1.register()

    student2 = Student("", 20, "Mathematics")
    student2.register()

    student3 = Student("Bob", -5, "Physics")
    student3.register()

    student4 = Student("Charlie", 22, "")
    student4.register()