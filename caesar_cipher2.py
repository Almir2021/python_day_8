alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar (start_text, shift_amount, chipher_direction):
   end_text =""
  
   for letter in start_text:
     shift_amount = abs(shift_amount)
     position = alphabet.index(letter)
     if chipher_direction == "decode":
       shift_amount *= -1
       print(shift_amount)
     new_position = position + shift_amount
     end_text += alphabet[new_position]
   print(f"here's the {direction}d result: {end_text} ")   




caesar (start_text=text, shift_amount=shift, chipher_direction=direction )