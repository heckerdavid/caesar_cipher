from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


def test_version():
    assert __version__ == '0.1.0'

def test_import():
    assert encrypt
    assert decrypt
    assert crack

def test_encrypt():
    actual = encrypt('i', 1)
    expected = 'j'
    assert actual == expected

def test_encrypt_2():
    actual = encrypt('hi', 1)
    expected = 'ij'
    assert actual == expected


def test_encrypt_3():
    actual = encrypt('hello world', 1)
    expected = 'ifmmp xpsme'
    assert actual == expected

def test_encrypt_key():
    actual = encrypt('hi', 2)
    expected = 'jk'
    assert actual == expected

def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected


def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected


def test_encrypt_shift_20():
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected

def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected

def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected

def test_with_non_alpha():
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected

def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected

def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected


def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = ""
    assert actual == expected