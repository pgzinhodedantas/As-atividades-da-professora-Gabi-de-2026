def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    
    if saque > 1000:
        taxa = saque * 0.50
        saldo_restante = saldo - saque - taxa
    else:
        saldo_restante = saldo - saque
    
    return saldo_restante