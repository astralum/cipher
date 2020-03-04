alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("What is your message? English alphabets only.\n> ")
num = int(input("\nBy how many spaces to the right? Integers only.\n> "))

def code(message, num):
    coded = ""
    lowercase = message.lower()

    for i in range(0,len(message)):
        if message[i] == " ": # check if it's a space
            decoded_letter = " "
        else:
            new_index = alphabet.find(lowercase[i]) + num

            if new_index>26: # check if the new index is out of range of alphabet
                while new_index>26:
                    new_index -= 26
            elif new_index<0:
                while new_index<0:
                    new_index += 26

            decoded_letter = alphabet[new_index]

        if message[i].isupper() == True: # make originally uppercase characters uppercase
            decoded_letter = decoded_letter.upper()

        coded += decoded_letter
        i += 1
    print(f"\nOutput is:\n{coded}")

code(message, num)
