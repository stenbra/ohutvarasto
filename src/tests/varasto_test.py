import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_lisays_maara_negatiivi(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_lisays_liika(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_ottaminen_liika_palauttaa_kaikki_mita_voidan(self):
        self.varasto.lisaa_varastoon(8)
        
        saatu_maara = self.varasto.ota_varastosta(9)
        
        self.assertAlmostEqual(saatu_maara,8)
        
    def test_ottaminen_maara_on_negatiivi(self):
        self.varasto.lisaa_varastoon(8)
        
        saatu_maara = self.varasto.ota_varastosta(-1)
        
        self.assertAlmostEqual(saatu_maara,0)
        
    def test_alku_saldo_negatiivi(self):
        varasto = Varasto(10,-1)
        
        self.assertAlmostEqual(varasto.saldo,0)
        
    def test_alku_saldo_liika(self):
        varasto = Varasto(10,200)
        
        self.assertAlmostEqual(varasto.saldo,10)
        
    def test_tilavuus_negatiivi(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus,0)
        
    def test_tilavuus_nolla(self):
        varasto = Varasto(0)
        
        self.assertAlmostEqual(varasto.tilavuus,0)
        
    def test__str__(self):
        self.assertAlmostEqual(self.varasto.__str__(),f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
