import math

def calcular_tintas():
    print('=' * 60)
    print(f'{"LOJA DE TINTAS - OTIMIZAÇÃO DE COMPRA":^60}')
    print('=' * 60)

    # Entrada de dados
    area = float(input('Digite o tamanho da área a ser pintada (m²): '))

    # Regras de negócio / Constantes
    COBERTURA_POR_LITRO = 6
    CAPACIDADE_LATA = 18.0
    PRECO_LATA = 80.00
    CAPACIDADE_GALAO = 3.6
    PRECO_GALAO = 25.00

    # 1. Cálculo base com 10% de folga
    litros_necessarios = (area / COBERTURA_POR_LITRO) * 1.10

    # -------------------------------------------------------------
    # Cenário 1: Comprar apenas latas de 18L
    # -------------------------------------------------------------
    latas_apenas = math.ceil(litros_necessarios / CAPACIDADE_LATA)
    custo_latas_apenas = latas_apenas * PRECO_LATA

    # -------------------------------------------------------------
    # Cenário 2: Comprar apenas galões de 3,6L
    # -------------------------------------------------------------
    galoes_apenas = math.ceil(litros_necessarios / CAPACIDADE_GALAO)
    custo_galoes_apenas = galoes_apenas * PRECO_GALAO

    # -------------------------------------------------------------
    # Cenário 3: Misturar latas e galões (menor custo / desperdício)
    # -------------------------------------------------------------
    # Pegamos a parte inteira de quantas latas cheias podemos usar
    latas_mistas = int(litros_necessarios // CAPACIDADE_LATA)
    
    # Calculamos o volume que sobrou após usar as latas inteiras
    litros_restantes = litros_necessarios % CAPACIDADE_LATA
    
    # Arredondamos a sobra em galões para cima
    galoes_mistos = math.ceil(litros_restantes / CAPACIDADE_GALAO)
    
    custo_misto = (latas_mistas * PRECO_LATA) + (galoes_mistos * PRECO_GALAO)

    # -------------------------------------------------------------
    # Exibição dos Resultados
    # -------------------------------------------------------------
    print('\n' + '-' * 60)
    print(f'Área informada: {area:.2f} m²')
    print(f'Tinta necessária (com 10% de folga): {litros_necessarios:.2f} L')
    print('-' * 60)

    print('\n1) COMPRANDO APENAS LATAS (18L):')
    print(f'   - Quantidade: {latas_apenas} lata(s)')
    print(f'   - Valor total: R$ {custo_latas_apenas:.2f}'.replace('.', ','))

    print('\n2) COMPRANDO APENAS GALÕES (3,6L):')
    print(f'   - Quantidade: {galoes_apenas} galão(ões)')
    print(f'   - Valor total: R$ {custo_galoes_apenas:.2f}'.replace('.', ','))

    print('\n3) COMPRA OTIMIZADA (MISTURA DE LATAS E GALÕES):')
    print(f'   - Quantidade: {latas_mistas} lata(s) e {galoes_mistos} galão(ões)')
    print(f'   - Valor total: R$ {custo_misto:.2f}'.replace('.', ','))
    print('-' * 60)

if __name__ == '__main__':
    calcular_tintas()