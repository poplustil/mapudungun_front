import json

# pipeline front-end

# diccionario pronunciacion de letras aisladas

# funcion para normalizacion de numeros
# input: numero
# output: palabras para nombrar al numero
def normalizeNumbers(number_word):
    with open('dict_nums.json') as data_file:
        numbers = json.load(data_file)

    return numbers[number_word]

# reglas LTS
# input: archivo de texto con el siguiente formato
# output: una estructura de datos que usara la funcion de transcripcion fonetica
def getLTS(lts_file):
    lts_dict = {}
    digraphs = []
    with open(lts_file) as data_file:
        for line in data_file:
            (key, val) = line.split()
            lts_dict[key] = val

    [digraphs.append(n[0]) for n in lts_dict.values() if len(n) > 1 and n[0] not in digraphs]

    return lts_dict, digraphs

# funcion para hacer transcripcion fonetica
# input: palabra, grafemario
# output: transcripcion fonetica de una palabra

# reglas de silibifacion
# input: archivo de texto con el siguiente formato
# output: una estructura de datos que usara la funcion de silibificacion

# funcion para silibificar
# input: transcripcion fonetica de una palabra
# output: transcripcion fonetica silibificada de una palabra

# reglas de acentuacion
# input: archivo de texto con el siguiente formato
# output: una estructura de datos que usara la funcion de acentuacion

# funcion para acentuar
# input: transcripcion fonetica silibificada
# output: transcripcion fonetica silibificada y acentuada de una palabra

# reglas post-lexicas
# input: archivo de texto con el siguiente formato
# output: una estructura de datos que usara la funcion de postlex

# funcion para aplicar reglas postlex
# input: oracion transcrita, silabificada y acentuada
# output: oracion con cambios postlex incluidos

# funcion para incluir in POS tagger
# input: pos tagger de nltk y palabra
# output: palabra y pos tag

# funcion para generar estructura linguistica para cada oracion
# input: oracion
# output: estructura que contiene el analisis linguistico de esa oracion

#---- Funciones benri

# funcion que tiene como input un corpus y selecciona las oraciones con mayor coverage

# funcion para crear un MLF a partir del script

# funcion que mide el coverage de un script

# funcion que mide el coverage de un mlf

# funcion para crear etiquetas HTS para cada oracion
