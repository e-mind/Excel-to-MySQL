import re
from apps.encriptador import encriptador
def proceso(frase):
    ex = re.compile('[A-Za-z0-9\s\ñ\Ñ]')
    final =''
    acumulador =''
    i = 0
    a = False
    for eachletter in frase:
        if eachletter == '>' or a == True:
            if a == False:
                acumulador = acumulador + eachletter
                a = True
            else:
                if i<=3:
                    if eachletter =='°':
                        acumulador = acumulador + eachletter
                        i = 1 + i
                    elif eachletter == '<':
                        acumulador = acumulador + eachletter
                        final = final + encriptador.encriptar(acumulador)
                        acumulador = ''
                        i=0
                        a=False
                    elif eachletter !='°':
                        acumulador = acumulador + eachletter
                        a=False
                        for cadapalabra in acumulador:
                            valido = ex.findall(cadapalabra)
                            if valido:
                                final = final + encriptador.encriptar(cadapalabra)
                            else:
                                final = final+cadapalabra
                                acumulador = ''
                else:
                    acumulador = acumulador + eachletter
                    for cadapalabra in acumulador:
                        valido = ex.findall(cadapalabra)
                        if valido:
                            final = final + encriptador.encriptar(cadapalabra)
                        else:
                            final = final+cadapalabra
                            acumulador = ''
                            a=False
        else:
            valido = ex.findall(eachletter)
            if valido:
                final = final + encriptador.encriptar(eachletter)
            else:
                final = final+eachletter
    return final
