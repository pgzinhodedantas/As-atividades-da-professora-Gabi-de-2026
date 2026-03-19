def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"
    elif usuario == "admin" and senha == "9020":
        return "Acesso total"
    elif usuario == "admin":
        return "Senha incorreta"
    else:
        return "Usuário inválido"

