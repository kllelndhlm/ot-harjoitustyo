import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luotu_paate_on_ajantasalla_rahaa(self):
        self.kassapaate = Kassapaate()
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

    def test_luotu_paate_on_ajantasalla_edulliset(self):
        self.kassapaate = Kassapaate()
        self.assertEqual(int(self.kassapaate.edulliset), 0)

    def test_luotu_paate_on_ajantasalla_maukkaat(self):
        self.kassapaate = Kassapaate()
        self.assertEqual(int(self.kassapaate.maukkaat), 0)

    def test_edullisesti_kateisella_riittavasti_rahamaara_kasvaa(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100240)

    def test_edullisesti_kateisella_riittavasti_vaihtoraha_oikein(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(int(self.kassapaate.syo_edullisesti_kateisella(250)), 10)

    def test_edullisesti_kateisella_ei_riittavasti_rahamaara_ei_muutu(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_edullisesti_kateisella(20)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

    def test_edullisesti_kateisella_ei_riittavasti_rahat_palautuvat(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_edullisesti_kateisella(20)
        self.assertEqual(int(self.kassapaate.syo_edullisesti_kateisella(20)), 20)

    def test_edullisesti_kateisella_ei_riittavasti_myydyt_ei_muutu(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_edullisesti_kateisella(20)
        self.assertEqual(int(self.kassapaate.edulliset)+int(self.kassapaate.maukkaat), 0)

    def test_maukkaasti_kateisella_riittavasti_rahamaara_kasvaa(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100400)

    def test_maukkaasti_kateisella_riittavasti_vaihtoraha_oikein(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(int(self.kassapaate.syo_maukkaasti_kateisella(450)), 50)

    def test_maukkaasti_kateisella_ei_riittavasti_rahamaara_ei_muutu(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_maukkaasti_kateisella(20)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

    def test_maukkaastii_kateisella_ei_riittavasti_rahat_palautuvat(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_maukkaasti_kateisella(20)
        self.assertEqual(int(self.kassapaate.syo_maukkaasti_kateisella(20)), 20)

    def test_maukkaasti_kateisella_ei_riittavasti_myydyt_ei_muutu(self):
        self.kassapaate = Kassapaate()
        self.kassapaate.syo_maukkaasti_kateisella(20)
        self.assertEqual(int(self.kassapaate.edulliset)+int(self.kassapaate.maukkaat), 0)

    def test_kortti_palauttaa_tosi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertTrue(str(self.maksukortti.ota_rahaa(10)), True)

    def test_kortin_saldo_vahenee_oikein_jos_rahaa_tarpeeksi_edulliseen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_kortilla_edullisten_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(int(self.kassapaate.edulliset), 1)

    def test_kortilla_ei_varaa_edulliseen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), False)

    def test_kortilla_ei_varaa_edulliseen_ei_veloiteta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) #saldo riittää neljään edulliseen
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) #viidettä ei veloiteta
        self.assertEqual(str(self.maksukortti), "saldo: 0.4")

    def test_kortilla_ei_varaa_edulliseen_myydyt_muuttumaton(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) #saldo riittää neljään edulliseen
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) #viidettä ei myydä
        self.assertEqual(int(self.kassapaate.edulliset)+int(self.kassapaate.maukkaat), 4)


    def test_kortin_saldo_vahenee_oikein_jos_rahaa_tarpeeksi_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_kortilla_maukkaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(int(self.kassapaate.maukkaat), 1)

    def test_kortilla_ei_varaa_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) #saldo riittää kolmeen maukkaaseen
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) #neljättä ei veloiteta
        self.assertTrue(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), False)

    def test_kortilla_ei_varaa_maukkaaseen_myydyt_muuttumaton(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) #saldo riittää kahteen  maukkaaseen
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) #kolmatta ei myydä
        self.assertEqual(int(self.kassapaate.edulliset)+int(self.kassapaate.maukkaat), 2)


    def test_kortilla_ei_varaa_maukkaaseen_ei_veloiteta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) #saldo riittää kahteen  maukkaaseen
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) #kolmatta ei myydä
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_rahamaara_ei_muutu_korttiostoksesta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

    def test_kortin_saldo_muuttuu_ladattaessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 12345)
        self.assertEqual(str(self.maksukortti), "saldo: 133.45")

    def test_rahamaara_muuttuu_ladattaessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 12345)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 112345)

    def test_rahamaara_ei_muutu_ladattaessa_miinusta(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertTrue(str(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)), None)

