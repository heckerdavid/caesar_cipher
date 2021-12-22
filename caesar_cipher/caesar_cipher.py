from caesar_cipher.corpus_loader import name_list, word_list

def encrypt(text, key):

    unshifted_alphabet = "abcdefghijklmnopqrstuvwxyz"
    unshifted_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    shifted_alphabet = unshifted_alphabet[key:] + unshifted_alphabet[:key]
    shifted_caps = unshifted_caps[key:] + unshifted_caps[:key]

    transformation = str.maketrans(unshifted_alphabet, shifted_alphabet)
    lower = text.translate(transformation)

    upper_transformation = str.maketrans(unshifted_caps, shifted_caps)

    lower_and_upper = lower.translate(upper_transformation)

    
    return lower_and_upper

def decrypt(encrypted_text, key):
    return encrypt(encrypted_text, -key)

def crack(encrypted_text):

    for i in range(26):
        total = 0
        test_text = encrypt(encrypted_text, i)
        text_as_a_list = test_text.split()
        for text in text_as_a_list:
            if text in name_list or text.lower() in word_list:
                total += 1
        
        if (total / len(text_as_a_list)) > .5:
            return ' '.join(text_as_a_list)

    return ''