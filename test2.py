import caesar_cipher
alphabet = caesar_cipher.alphabet

alphabet = caesar_cipher.alphabet
direction = 'encode'  # Hardcoded value for testing
text = 'abc'  # Hardcoded value for testing
shift_amout = 1  # Hardcoded value for testing


plain_text = "abz"
plain_text = list(plain_text)

shifted_word = []
where_letters = [] 

print(plain_text)

for letter in plain_text:
     where_letters.append(alphabet.index(letter))
      
print(where_letters)

for letter in where_letters:
     if letter < shift_amout:
         where_letters[letter] = where_letters[ letter] +25 

       # for some reasone index is out of range look in to it. 
     #where_letters[letter] = where_letters[letter] - shift_amout     
for letter in where_letters:
    print(letter)
   # where_letters[letter]= where_letters[letter]-shift_amout 
print(where_letters)        
print(alphabet[25])  