class Internet:
    def __init__(self, nama, paket, harga):
        self.nama = nama
        self.paket = paket
        self.harga = harga

    def get_tagihan(self):
        return self.harga 

pelanggan = Internet("Kevien" , "Paket Jitu 1", "Rp.5000") 
print(f"Nama : {pelanggan.nama}")
print(f"Paket : {pelanggan.paket}")
print(f"Harga : {pelanggan.get_tagihan()}")