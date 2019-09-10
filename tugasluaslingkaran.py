class LuasLingkaran(object):
    def __init__(self, phi, r):
        self.phi = phi
        self.jarijari = r
    def hitungLuas(self):
        return self.phi * self.jarijari**2

def main():
    luasLingkaran1 = LuasLingkaran(3.14, 3)

    print('Objek luaslingkaran1')
    print('phi\t        : ', luasLingkaran1.phi)
    print('jari-jari\t: ', luasLingkaran1.jarijari)
    print('luas\t= ', luasLingkaran1.hitungLuas())

    luasLingkaran2 = LuasLingkaran(3.14, 6)

    print("\nObjek luaslingkaran2")
    print("phi\t        : ", luasLingkaran2.phi)
    print("jari-jari\t: ", luasLingkaran2.jarijari)
    print("luas\t= ", luasLingkaran2.hitungLuas())

if __name__ == "__main__":
    main()
    
    
