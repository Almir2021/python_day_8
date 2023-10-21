alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Don't change the code above 👆
count_l = 0
where_letters = [] 
shifted_word = []
shifted_string = " "
cipher_text = " "
count_l2 =[]
shifted_string2 = " " 
shift_amount = 0
# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):

#  TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
#   e.g. 
#   plain_text = "hello"
#   shift = 5
#   cipher_text = "mjqqt"
#   print output: "The encoded text is mjqqt"      
      
      
      
      
      plain_text = list(plain_text)
      print(plain_text)
      for n in plain_text:
            count_l = 0
            for l in alphabet:
              count_l +=1
              if n == l :
                   where_letters.append(count_l)
                   break
      for e in range(len(where_letters)):
           where_letters[e] += (shift_amount-1)
           shifted_word.append(alphabet[where_letters[e]])
      
      cipher_text = shifted_string.join(shifted_word)
      print(f"The encoded text is  {cipher_text}")
      #print(type(cipher_text))
                       
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    
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
      if where_letters[l] < shift_amount:
          where_letters[l] += 26
          where_letters[l] = where_letters[l]-shift_amount
      else :
          where_letters[l] = where_letters[l]-shift_amount

      shifted_word.append(alphabet[where_letters[l]])    

  cipher_text = shifted_string.join(shifted_word)
  print(f"The encoded text is  {cipher_text}")
  print(type(cipher_text))
  print(where_letters)


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)
 
  
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. j