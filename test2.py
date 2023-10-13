import caesar_cipher
alphabet = caesar_cipher.alphabet

alphabet = caesar_cipher.alphabet
direction = 'encode'  # Hardcoded value for testing
text = 'abc'  # Hardcoded value for testing
shift_amout = 5  # Hardcoded value for testing


plain_text = "hello"
plain_text = list(plain_text)

shifted_word = []
where_letters = [] 
shifted_word = []
shifted_string = ""
print(plain_text)

for letter in plain_text:
       if letter in plain_text:
         where_letters.append(alphabet.index(letter))

for l in range(0,len(where_letters)):
    if where_letters[l] < shift_amout:
        where_letters[l] += 26
        where_letters[l] = where_letters[l]-shift_amout
    else :
        where_letters[l] = where_letters[l]-shift_amout

    shifted_word.append(alphabet[where_letters[l]])    

cipher_text = shifted_string.join(shifted_word)
print(f"The encoded text is  {cipher_text}")
print(type(cipher_text))
print(where_letters)