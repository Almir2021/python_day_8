import caesar_cipher
alphabet = caesar_cipher.alphabet

alphabet = caesar_cipher.alphabet
direction = 'encode'  # Hardcoded value for testing
text = 'abc'  # Hardcoded value for testing
shift_amout = 1  # Hardcoded value for testing


plain_text = "abc"
plain_text = list(plain_text)

shifted_word = []
where_letters = [] 

print(plain_text)

  
      
plain_text = list(plain_text)
for n in plain_text:
            count_l = 0
            for l in alphabet:
              count_l +=1
              if n == l :
                   where_letters.append(count_l)
                   break
print(where_letters)                   
for e in range(len(where_letters)):
           where_letters[e] += shift_amout
           shifted_word.append(alphabet[where_letters[e-1]])

print(where_letters)
print(shifted_word)
                             



