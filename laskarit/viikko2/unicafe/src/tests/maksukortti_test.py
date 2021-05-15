import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alusa_oikein(self):
        maksukortti = Maksukortti(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(25)
        self.assertEqual(str(self.maksukortti), "saldo: 0.35")

    def test_saldo_vaehenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.lataa_rahaa(400)
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldo_ei_vaehene_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldo_ei_vaehene_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_palauttaa_tosi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertTrue(str(self.maksukortti.ota_rahaa(10)), True)

    def test_palauttaa_epaetosi(self):
        self.maksukortti.ota_rahaa(10000000)
        self.assertTrue(str(self.maksukortti.ota_rahaa(10000000)), False)