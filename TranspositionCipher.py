#Transposition Cipher
import math

def transpositionEncrypt(message, key):
    #Check if any transposing occurs
    if key >= len(message):
        print("No encryption occured. Key is longer than message.")
        return "0"
    else:      
        #Create a list of '' with key # of elements
        cipherText = [''] * key 
        #Loop through all chars in message
        for i in range(key):
            currentIndex = i
            while currentIndex < len(message):
                #Assign the correct transposed character to the appropriate column in our list.
                cipherText[i] += message[currentIndex]
                #Skip over to the next character in the message a number of times equal to our key.
                currentIndex += key 
        #Join all the columns of our text in our list together. Resulting in our encrypted text.
        return ''.join(cipherText)
    
def transpositionDecrypt(cipherMessage, key):
    #key = total number of rows
    #decryptKey = total number of columns
    
    #Find the new matrix number of Columns as the new decryption key.
    #We use the ceiling function because we want a square matrix accounting
    # for the empty spaces at the end.
    decryptKey = math.ceil(len(cipherMessage)/key)
    numEmptySpace = (decryptKey * key) - len(cipherMessage)
    if decryptKey >= len(cipherMessage):
        print("No decryption occured. Key is longer than message.")
        return "0"
    else:
        row = 0
        column = 0
        decryptedText = [''] * decryptKey
        #Loop through all chars in message
        for i in cipherMessage:
            #Assign the correct transposed character to the appropriate column in out list.
            decryptedText[column] += i
            column += 1
            #If the end of the columns are reached return to the beginning and one row down.
            #We also account for the empty spaces at the end of the last column and skip them.
            if (column == decryptKey) or (column == decryptKey - 1 and row >= key - numEmptySpace):
                column = 0
                row += 1
        #Returning the complete list of chars joined together resulting in our decrypted message.
        return ''.join(decryptedText)

#Example function calls

#encryptedMessage = transpositionEncrypt("Do not use pc", 8)
#print(encryptedMessage)
#decryptedMessage = transpositionDecrypt(encryptedMessage, 8)
#print(decryptedMessage)