import math

def bhaskara( a, b, c ):
    print(f"\n\n{a}•x²+{b}•x+{c}=0")
    delta = b ** 2 - 4 * a * c
    raiz_delta = math.sqrt( b ** 2 - 4 * a * c )
    print(f"\n ∆ = {delta}")
    print(f"\n √∆ = {raiz_delta}")
    x1 = ( - b + raiz_delta ) / ( 2 * a )
    x2 = ( - b - raiz_delta ) / ( 2 * a )
    
    print(f"\nS = ({x1};{x2})")

valor_a = int(input("\nDigite o valor de a: "))
valor_b = int(input("\nDigite o valor de b: "))
valor_c = int(input("\nDigite o valor de c: "))
bhaskara(valor_a, valor_b, valor_c)
