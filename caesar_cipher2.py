alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

def caesar (start_text, shift_amount, chipher_direction):
    end_text =""
    
    for char in start_text:
      if char in alphabet:
                shift_amount = abs(shift_amount)
                position = alphabet.index(char)
                if chipher_direction == "decode":
                 shift_amount *= -1
                new_position = (position + shift_amount) % 26
                end_text += alphabet[new_position]
      else :
          end_text += char        
    print(f"here's the {direction}d result: {end_text} ")   




should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  caesar (start_text=text, shift_amount=shift, chipher_direction=direction )
  result = input ("Type yes if you want to go again . Otherwise type 'no'.\n")
  if result == "no":
     should_continue = False
     print("Goodbye") 
