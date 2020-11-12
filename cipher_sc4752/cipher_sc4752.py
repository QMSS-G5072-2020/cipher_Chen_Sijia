def cipher(text, shift, encrypt=True):
    """
    This is a function to encipher or decipher the text by using Caesar cipher.
    
    Input:
    text: a string that you want to encrypt or decrypt. 
    shift: a number that can effect the way to encipher and decipher the text. Different shifts represent different way to encipher and decipher the text.
    encrypt: a boolean value whose default value is True. If encrypt is True, then the cipher function is to encipher the text. If encrypt is False, then the cipher function is to decipher the text.
    
    Output:
    The output is a new text that shows the result of the encipher or decipher.
    
    Examples:
    >>> from cipher_sc4752 import cipher_sc4752
    >>> cipher('abc',3,True)
    'def'
    >>> cipher('abc',3,False)
    'XYZ'

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text