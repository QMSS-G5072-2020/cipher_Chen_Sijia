from cipher_sc4752 import __version__
from cipher_sc4752 import cipher_sc4752

def test_version():
    assert __version__ == '0.1.0'

def test_cipher():
    example='abc'
    shift=3
    expected='def'
    actual=cipher_sc4752.cipher(example,shift)
    assert actual==expected