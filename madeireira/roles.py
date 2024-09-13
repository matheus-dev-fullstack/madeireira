from rolepermission.roles import AbstactUserRole

class Gerente(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedor': True,
        
    }