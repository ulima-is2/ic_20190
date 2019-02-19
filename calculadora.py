class Calculadora:
    '''
    Suma aritmetica que puede recibir
    enteros asi como numeros pero en
    string
    '''
    def sumar(self, op1, op2):
        if isinstance(op1, str) and isinstance(op2, str):
            return str(int(op1) + int(op2))
        elif isinstance(op1, int) and isinstance(op2, int):
            return op1 + op2
        else:
            return None

    def restar(self, op1, op2):
        return op1 - op2

    def dividir(self, op1, op2):
        if op2 != 0:
            return op1 / op2
        else:
            return None