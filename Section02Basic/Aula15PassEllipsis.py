"""

Pass e Ellipsis (...) como placeholders

"""

##-----------------------------------pass-----------------------------------##

valor = False

if valor:
    # Pula esse comando sem dar erro; Explicando algo que vou fazer posteriormente
    pass
else:
    print('Tchau')

##-----------------------------------ellipsis (...)-----------------------------------##
valor = False

if valor:
    ...  # Pula esse comando sem dar erro; Não foi feito para este fim.
else:
    print('Tchau')
