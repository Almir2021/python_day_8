# import caesar_cipher
# alphabet = caesar_cipher.alphabet

# alphabet = caesar_cipher.alphabet
# direction = 'encode'  # Hardcoded value for testing
# text = 'abc'  # Hardcoded value for testing
# shift_amout = 1  # Hardcoded value for testing


# plain_text = "abz"
# plain_text = list(plain_text)

# shifted_word = []
# where_letters = [] 

# print(plain_text)

  
      
# plain_text = list(plain_text)
# for n in plain_text:
#             count_l = 0
#             for l in alphabet:
#               count_l +=1
#               if n == l :
#                    where_letters.append(count_l)
#                    break
# print(where_letters)                   
# for e in range(len(where_letters)):
#            where_letters[e] += (shift_amout-1)
#            shifted_word.append(alphabet[where_letters[e]])

# print(where_letters)
# print(shifted_word)
                             
print("Lets play a game!")

dotheywantotplay = input("Do you want to play Rock-Paper-Scissors? (y or n) ")

if dotheywantotplay == "y":

    player1 = input('Enter first players name: ')
    player2 = input('Enter second players name: ')

    personchoice1 = input("What move will you do? [\"Rock\", \"Paper\", \"Scissors\"]")

    personchoice2 = input("What move will you do? [\"Rock\", \"Paper\", \"Scissors\"]")

    Play(personchoice1,personchoice2) # The error looks like its this line

else:
    print("I am so sad now :-(")
    exit()




class Play:
    def __init__(player1, player2):
        self.player1 = player1
        self.player2 = player2

        if player1 == player2:
                print("Tie!")
        elif player1 == "Rock":
            if player2 == "Paper":
                print("You lose!", player2, "covers", player1)
            else:
                print("You win!", player1, "smashes", player2)
        elif player1 == "Paper":
            if player2 == "Scissors":
                print("You lose!", player2, "cut", player1)
            else:
                print("You win!", player1, "covers", player2)
        elif player1 == "Scissors":
            if player2 == "Rock":
                print("You lose...", player2, "smashes", player1)
            else:
                print("You win!", player1, "cut", player2)
        else:
            print("That's not a valid play. Check your spelling!")


if dotheywantotplay == "y":

    player1 = input('Enter first players name: ')
    player2 = input('Enter second players name: ')

    personchoice1 = input("What move will you do? \"Rock\", \"Paper\", \"Scissors\"  ")
    personchoice2 = input("What move will you do? \"Rock\", \"Paper\", \"Scissors\"  ")

    Play(personchoice1,personchoice2, player1, player2)

else:
    print("I am sad now :-(")
    exit()