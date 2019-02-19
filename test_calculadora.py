import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_sumar_correcto(self):
        calculadora = Calculadora()
        op1 = 3
        op2 = 2
        res_obtenida = calculadora.sumar(op1, op2)
        res_esperada = 5
        self.assertEqual(res_obtenida, 
            res_esperada, 
            "Suma incorrecta: op1:{} op2:{} r_obtenido:{} r_esperado:{}".format(
                op1, op2, res_obtenida, res_esperada))

    def test_sumar_strings(self):
        calculadora = Calculadora()
        op1 = "3"
        op2 = "2"
        res_esperada = "5"
        res_obtenida = calculadora.sumar(op1, op2)
        self.assertEqual(res_esperada, res_obtenida, "Hay error")

    def test_sumar_int_str(self):
        calculadora = Calculadora()
        op1 = "3"
        op2 = 2
        res_esperada = None
        res_obtenida = calculadora.sumar(op1, op2)
        self.assertEqual(res_esperada, res_obtenida, "Hay error")

    def test_restar_correcto(self):
        calculadora = Calculadora()
        op1 = 3
        op2 = 2
        res_esperada = 1
        res_obtenida = calculadora.restar(op1, op2)
        self.assertEqual(res_esperada, res_obtenida)

    def test_restar_negativo(self):
        calculadora = Calculadora() 
        op1 = 2
        op2 = 4
        res_esperada = -2
        res_obtenida = calculadora.restar(op1, op2)
        self.assertEqual(res_esperada, res_obtenida)

    def test_dividir_entre_0(self):
        calculadora = Calculadora()
        op1 = 2
        op2 = 0
        res_esperada = None
        res_obtenida = calculadora.dividir(op1, op2)
        self.assertEqual(res_esperada, res_obtenida)
