class Ongkir:
  def checkOngkir(self,pengirim, penerima, jarak, berat):
    ongkir = berat * 5000 * jarak
    keterangan = f"Paket dikirim oleh {pengirim} ke {penerima} dengan jarak {jarak} km dan berat {berat} kg.Total Ongkir = " + str(ongkir)
    return keterangan
  

paketA = Ongkir()
paketA.pengirim = "Kevien"
paketA.penerima = "Budi"
paketA.jarak = 20
paketA.berat = 10
print(paketA.checkOngkir(paketA.pengirim, paketA.penerima, paketA.jarak, paketA.berat))