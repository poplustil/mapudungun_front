# -*- coding: utf-8 -*-
import json
import codecs
from collections import defaultdict

###### CLASES ######

# defalut dict: Por ahora, si el grafema no esta en LTS, devuelve el mismo valor
class defDict(dict):
    __missing__ = lambda self, key: key[0]

# data structure por oracion
class lingAnalisis(sentence):
    pass

###### FUNCIONES #####

# pipeline front-end

# diccionario pronunciacion de letras aisladas
# TODO

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
    lts_dict = defDict()
    digraphs = []
    with codecs.open(lts_file, encoding='utf-8') as data_file:
        for line in data_file:
            k1, k2, val = line.split()
            lts_dict[(k1, k2)] = val
            print val

    [digraphs.append(n[0]) for n in lts_dict.keys() if len(n[0]) > 1 and n[0] not in digraphs]

    return lts_dict, digraphs

# funcion para hacer transcripcion fonetica
# input: palabra, grafemario, lista de digrafos
# output: transcripcion fonetica de una palabra
# TODO: que pasa con las palabras en español?
def transcribe(word, graph_inv, lts_dict, digraph_list):
    PUNCT = '.,;:'
    phones = []
    flag = False
    for n in range(0, len(word)):
        if word[n] not in PUNCT:
            if n != len(word)-1:
                if flag == True:
                    flag = False
                elif word[n]+word[n+1] not in digraph_list and flag == False:
                    phones.append(lts_dict[(word[n],graph_inv)])
                else:
                    phones.append(lts_dict[(word[n]+word[n+1], graph_inv)])
                    flag = True
            else:
                phones.append(lts_dict[(word[n],graph_inv)])
    return phones

# TODO: identificar palabras en español para insertar schwa en grupos consonanticos en ataque
# funcion para silibificar
# input: transcripcion fonetica de una palabra
# output: transcripcion fonetica silibificada de una palabra
def syllabify(phone_list):
    C = ('f', 'k', 'l', 'lh', 'll', 'm', 'n', 'nh', 'ny', 'ng', 'p', 'r','s', 't', 'th', 'ch', 'tx')
    V = ('a', 'e' 'i', 'o', 'u', 'y')
    semi = ('j', 'w')
    oclAfr = ('ch', 'tx', 'p', 't', 'th', 'k')
    g = 'g'
    posSeq = ('V', 'VC', 'CV', 'CVC')

    syllabified = []
    for n in range(0, len(phone_list)):
        c = phone_list[n]
        p = phone_list[n-1]
        x = phone_list[n+1]





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
def getScript(corpus_path):
    text = codecs.open(corpus_path, encoding='utf-8').read().split('\n')
    lts_dict, digraphs = getLTS('LTS')
    for n in text:
        for i in n.split():
            phones = transcribe(i.lower(), 'azumfeche', lts_dict, digraphs)
            print syllabify(phones)


# funcion para crear un MLF a partir del script

# funcion que mide el coverage de un script

# funcion que mide el coverage de un mlf

# funcion para crear etiquetas HTS para cada oracion


#### MAIN ####
getScript('textosmapuches_primerobasico.txt')
