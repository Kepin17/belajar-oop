class Ongkir:
    def __init__(self, penngirim, penerima, jarak, berat):
        self.pengirim = penngirim
        self.penerima = penerima
        self.jarak = jarak
        self.berat = berat

    def checkOngkir(self):
        ongkir = self.berat * 5000 * self.jarak
        keterangan = f"Paket dikirim oleh {self.pengirim} ke {self.penerima} dengan jarak {self.jarak} km dan berat {self.berat} kg.Total Ongkir yang harus dibayarkan adalah Rp." + str(ongkir)
        return keterangan

paketA = Ongkir("Kevien", "Budi", 20, 10)
print(paketA.checkOngkir())

        