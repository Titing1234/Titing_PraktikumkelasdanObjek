class kelilingLingkaran(object):
    def __init__(self, r, p):
        self.jarijari = r
        self.phi = p
    def hitungKeliling(self):
        return 2 * self.phi * self.jarijari
    def cetakData(self):
        print("jari-jari\t: ", self.jarijari)
        print("phi\t: ", self.phi)
    def cetakKeliling(self):
        print("Keliling\t= ", self.hitungKeliling())

def main():

    KLingkaran1 = kelilingLingkaran(45,3.14)
    print("Objek Lingkaran1")
    KLingkaran1.cetakData()
    KLingkaran1.cetakKeliling()

    KLingkaran2 = kelilingLingkaran(49,22/7)
    print("\nObjek Lingkaran2")
    KLingkaran2.cetakData()
    KLingkaran2.cetakKeliling()

if __name__ == "__main__":
    main()
                            
