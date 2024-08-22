import libreriaComplejos as lc
import unittest

class TestCplxOperations(unittest.TestCase):

    def test_sumacplx(self):
        suma = lc.sumacomplejos((1,2),(-5,4.3))
        self.assertAlmostEqual(suma[0],-4)
        self.assertAlmostEqual(suma[1],6.3)

    def test2_sumacplx(self):
        suma = lc.sumacomplejos((1,5),(7,20.4))
        self.assertAlmostEqual(suma[0],8)
        self.assertAlmostEqual(suma[1],25.4)

    def test_multicplx(self):
        produ1,produ2 = lc.multiplicacion((1.3,7),(-5,6))
        self.assertAlmostEqual(produ1,-34.4)
        self.assertAlmostEqual(produ2,92.7)
        

    def test2_multicplx(self):
        produ1,produ2 = lc.multiplicacion((1.3,7),(-5,6))
        self.assertAlmostEqual(produ1,-48.5)
        self.assertAlmostEqual(produ2,58)

    def test_restacplx(self):
        res1,res2 = lc.resta((12,-7.2),(-8,8))
        self.assertAlmostEqual(res1,20)
        self.assertAlmostEqual(res2,-15.2)

    def test2_restacplx(self):
        res1,res2 = lc.resta((2,72),(15,55))
        self.assertAlmostEqual(res1,-13)
        self.assertAlmostEqual(res2,17)

    def test_divisioncplx(self):
        div1,div2 = lc.division((1,2),(4,5))
        self.assertAlmostEqual(div1,0.5454545454545454)
        self.assertAlmostEqual(div2,-0.18181818181818182)

    def test2_divisioncplx(self):
        div1,div2 = lc.division((12.2,45),(3,8))
        self.assertAlmostEqual(div1,-323.4)
        self.assertAlmostEqual(div2,-225.0)
    
    def test_modulocplx(self):
        mod = lc.modulo((15,6))
        self.assertAlmostEqual(mod,16.15)
        
    def test2_modulocplx(self):
        mod = lc.modulo((5,1))
        self.assertAlmostEqual(mod,5.385)
        
    def test_conjugadocplx(self):
        conj1,conj2 = lc.conjugado((7,-5),(-1,-1.5))
        self.assertAlmostEqual(conj1[0][1],5)
        self.assertAlmostEqual(conj2[1][1],-1.5)

    def test2_conjugadocplx(self):
        conj1,conj2 = lc.conjugado((4,2),(-2,5.2))
        self.assertAlmostEqual(conj1[0][1],-2)
        self.assertAlmostEqual(conj2[1][1],-5.2) 
    
    def test_polarcplx(self):
        pol = lc.polar((1,2))
        self.assertAlmostEqual(pol[0],2.2)
        self.assertAlmostEqual(pol[1],1.1)

    def test2_polarcplx(self):
        pol = lc.polar((7,5))
        self.assertAlmostEqual(pol[0],3)
        self.assertAlmostEqual(pol[1],1.9)
    
    def test_cartesianocplx(self):
        car = lc.cartesiano((5,1))
        self.assertAlmostEqual(car[0],4.9)
        self.assertAlmostEqual(car[1],1.0)

    def test2_cartesianocplx(self):
        car = lc.cartesiano((12,10))
        self.assertAlmostEqual(car[0],12)
        self.assertAlmostEqual(car[1],10)

    def test_fasecplx(self):
        fas = lc.fase((5,2))
        self.assertAlmostEqual(fas,0.3)
        

    def test2_fasecplx(self):
        fas = lc.fase((2,8))
        self.assertAlmostEqual(fas,1.3)
        

    

if __name__ == '__main__':
    unittest.main()