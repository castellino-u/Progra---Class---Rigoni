import pytest
from programas import*
#EJERCICIO 1
@pytest.mark.parametrize("num, resp",[
    (94219667, True),
    (9, False),
    (41417055, True),
])
def test_validDni(num, resp):
    assert validDni(num) == resp
#EJERCICIO 2
@pytest.mark.parametrize("name, resp",[
    (["Ruth", "Condorí"], "Condorí")
])
def test_search_last_name(name, resp):
    assert search_last_name(name) == resp


@pytest.mark.parametrize("dni, resp",[
    (94219667, 942),
    (9421966, 942)
])
def test_get_dni_id(dni, resp):
    assert get_dni_id(dni) == resp

@pytest.mark.parametrize("name, last_name, num_id, resp",[
    (["Paula", "Geier"], "Geier", 445, "Paula5445")
])
def test_create_id(name, last_name, num_id, resp):
    assert create_id(name, last_name, num_id) == resp
#EJERCICIO 3    
#EJERCICIO 4
# test_calculadora.py
def test_multiples1(): # Caso de prueba 1: a es múltiplo de b 
    assert Multiples(10, 2) == True
# Caso de prueba 2: b es múltiplo de a 
def test_multiples2(): # Caso de prueba 2: a no múltiplo de b 
    assert Multiples(7, 2) == False

#EJERCICIO 5
#EJERCICIO 6
def space_word_test1():
    assert space_between_letters('Hola, tu') == 'H o l a, t u'

def space_word_test2():
    assert space_between_letters('Hola, jaja') == 'H o l a, j a j a'

#EJERCICIO 7
#EJERCICIO 8
#EJERCICIO 9
#EJERCICIO 10
@pytest.mark.parametrize('a,res',[
    ({1000:0.10,2000:0.20,3000:0.30,1500:0.10,2500:0.20,3500:0.30},10400),
    ({1500:0.15,2500:0.25,3500:0.35,1550:0.15,2550:0.25,3550:0.35},10962.5)
])
def test_purchase_total(a,res):
    assert purchase_total(a)==res
#EJERCICIO 11
#EJERCICIO 12
from tp5 import phrase_to_dict

# Prueba para una frase simple
def test_phrase_to_dict_simple():
    phrase = "Hello World"
    result = phrase_to_dict(phrase)
    expected = {"Hello": 5, "World": 5}
    assert result == expected

# Prueba para una frase con palabras de diferentes longitudes
def test_phrase_to_dict_varied_lengths():
    phrase = "The quick brown fox jumps over the lazy dog"
    result = phrase_to_dict(phrase)
    expected = {"The": 3, "quick": 5, "brown": 5, "fox": 3, "jumps": 5, "over": 4, "the": 3, "lazy": 4, "dog": 3}
    assert result == expected

#EJERCICIO 13
#EJERCICIO 14
#EJERCICIO 15
#EJERCICIO 16