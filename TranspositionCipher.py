#Transposition Cipher
#TO DO  Add file system that automates all file format naming 
import math, time, os, sys

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

def main():
    print("Enter .txt file name for encryption/decryption:")
    inputFileName = input("> ")
    fileNameWithExtension = inputFileName + ".txt"
    print("Enter public key number:")
    myKey = int(input("> " ))
    
    
    #Modes: 'encrypt', 'decrypt'
    print("(E)ncrypt Mode, (D)ecrypt Mode")
    modeKey = input("> ")
    mode = "Default"
    while not (modeKey.lower() == "e" or modeKey.lower() == "d"):
        print("Incorrect Entry:\n(E)ncrypt Mode, (D)ecrypt Mode")
        modeKey = input("> ")
    
    if modeKey.lower() == "e":
        mode = "Encrypt"
         #Will overwrite original files
        outputFileName = "%s.Encrypted.txt" % (inputFileName)
    elif modeKey.lower() == "d":
        mode = "Decrypt"
        outputFileName = "%s.Decrypted.txt" % (inputFileName)
    
    #Check if the input file name exists, or exit program
    if not os.path.exists(fileNameWithExtension):
        print('The file %s does not exist. Quitting . . .' % (fileNameWithExtension))
        sys.exit()
        
    #Give user option to exist program if the output file name already exists to avoid overwriting
    if os.path.exists(outputFileName):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit?" % (outputFileName))
        response = input("> ")
        while not (response.lower().startswith("c") or response.lower().startswith("q")):
            print("Incorrect entry.\nThis will overwrite the file %s. (C)ontinue or (Q)uit?")
            if response.lower().startswith("c") or response.lower().startswith("q"):
                break
        if response.lower().startswith("q"):
            sys.exit()
        if response.lower().startswith("c"):
            print("Importing file's contents for encryption. . .")
            
    #Read in message from input file
    fileObj = open(fileNameWithExtension)
    rawFileContent = fileObj.read()
    fileObj.close()
    
    print("File content imported.")
    
    print("%sing" % (mode.title()))
    
    #Start encryption/decryptiion timer
    startTime = time.time()
    
    if mode == "Encrypt":
        translated = transpositionEncrypt(rawFileContent, myKey)
    elif mode == "Decrypt":
        translated = transpositionDecrypt(rawFileContent, myKey)
    
    #End encryption/decryption timer
    totalTime = round(time.time() - startTime, 2)
    print("%sion time: %s seconds" % (mode.title(), totalTime)) 
    
    #Write translated content to an output file
    outputFileObj = open(outputFileName, "w")
    outputFileObj.write(translated)
    outputFileObj.close()
    
    print("Done %sing %s (%s characters)." % (mode, fileNameWithExtension, len(rawFileContent)))

# Call the main function if the program is run instead of imported as a module
if __name__ == '__main__':
    main()