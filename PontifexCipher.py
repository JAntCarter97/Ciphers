#Pontifex Cipher A.K.A Solitare 

import numpy as np 

textDict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V",
23: "W", 24: "X", 25: "Y", 26: "Z"}

textKeys = np.array(list(textDict.keys()))
textValues = np.array(list(textDict.values()))

cardDict = {1: "Ac", 2: "2c", 3: "3c", 4: "4c", 5: "5c", 6: "6c", 7: "7c", 8: "8c", 9: "9c", 10: "10c",
11: "Jc", 12: "Qc", 13: "Kc", 14: "Ad", 15: "2d", 16: "3d", 17: "4d", 18: "5d", 19: "6d", 20: "7d",
21: "8d", 22: "9d", 23: "10d", 24: "Jd", 25: "Qd", 26: "Kd", 27: "Ah", 28: "2h", 29: "3h", 30: "4h",
31: "5h", 32: "6h", 33: "7h", 34: "8h", 35: "9h", 36: "10h", 37: "Jh", 38: "Qh", 39: "Kh", 40: "As",
41: "2s", 42: "3s", 43: "4s", 44: "5s", 45: "6s", 46: "7s", 47: "8s", 48: "9s", 49: "10s", 50: "Js",
51: "Qs", 52: "Ks", 53: "JOKa", 54: "JOKb"}

cardKeys = np.array(list(cardDict.keys()))
cardValues = np.array(list(cardDict.values()))
     
#Custom Modulo funtion
def custom_modulo(n, mod):
    result = n % mod
    return result if result != 0 else mod
                
#PONTIFEX Method
def pontifexCipher(message, isEncryptMode, deckOrderArg = list(cardDict.values())):
    deckOrder = deckOrderArg
    #Remove all whitespace and capitalize all characters
    message = message.replace(" ", "")
    message = message.upper()
    #Empty list for the output line
    outputLine = []
    #Empty list for the new converted message values
    messageNums = []
    #Convert message to text number values
    for i in message:
        for k in textValues:
            if i == k:
                messageNums.append(np.where(textValues == k)[0][0]+1)
    #print(messageNums)
    
    #ALgorithm:
    # Shift Joker A down 1 card. Bottom card position serves as the top card position (cyclic). 
    # Shift Joker B down 2 cards.
    # Triple Cut: Swap the cards above the top joker and below the bottom joker
    # Count Cut: Count down from the top equal to the cardDict key number of the bottom card,
    #            then cut the deck at that counted down index while keeping the bottom card 
    #            at the bottom.
    # Output Line: Count down from the top equal to the cardDict key number of the Top card,
    #              if the card you counted down to is a joker then start the algorithm from
    #              the beginning, if not a joker then that card's cardDict key number is the
    #              output. 
    # Repeat algorithm as many times as characters in the cipher/message text.
    
    print(deckOrder)
    print()
    l = 0
    while l < len(message):
        
        #Shift Joker A down 1
        print("Shifting Joker A down 1")
        for i in deckOrder:
            if i == "JOKa":
                indexNum = deckOrder.index(i)
                newIndexNum = (indexNum + 1) % 54
                #List boundary end checks so python lists are removing the right indexes
                if deckOrder.index(i) != 53:             
                    deckOrder.insert(newIndexNum + 1, i)
                    deckOrder.pop(indexNum)
                elif deckOrder.index(i) == 53:
                    deckOrder.insert(newIndexNum + 1, i)
                    deckOrder.pop(indexNum + 1)
                break 
            
        print(deckOrder)
        print()

        #Shift Joker B down 2
        print("Shifting Joker B down 2")
        for i in deckOrder:
            if i == "JOKb":
                indexNum = deckOrder.index(i)
                newIndexNum = (indexNum + 2) % 54
                #List boundary end checks so python lists are removing the right indexes
                if deckOrder.index(i) >= 52:
                    deckOrder.insert(newIndexNum + 1, i)
                    deckOrder.pop(indexNum + 1)
                else:
                    deckOrder.insert(newIndexNum + 1, i)
                    deckOrder.pop(indexNum)
                break
        
        print(deckOrder)
        print()

        # Triple Cut: Swap the cards above the top joker and below the bottom joker
        print("Performing a Triple Cut")
        jokerAindex = 0
        jokerBindex = 0
        for i in deckOrder:
            if i == "JOKa":
                jokerAindex = deckOrder.index(i)
        for i in deckOrder:
            if i == "JOKb":
                jokerBindex = deckOrder.index(i)
        if jokerAindex < jokerBindex:
            deckTop = deckOrder[0:jokerAindex]
            deckMiddle = deckOrder[jokerAindex : jokerBindex + 1]
            deckBottom = deckOrder[jokerBindex + 1 : len(deckOrder)]
            deckOrder = deckBottom + deckMiddle + deckTop
            print(deckOrder)
        elif jokerAindex > jokerBindex:
            deckTop = deckOrder[0:jokerBindex]
            deckMiddle = deckOrder[jokerBindex : jokerAindex + 1]
            deckBottom = deckOrder[jokerAindex + 1 : len(deckOrder)]
            deckOrder = deckBottom + deckMiddle + deckTop
            print(deckOrder)
        print()

        # Count Cut: Count down from the top equal to the cardDict key number of the bottom card,
        #            then cut the deck at that counted down index while keeping the bottom card 
        #            at the bottom.
        print("Perforing a Count Cut")
        cardCount = 0
        for i in cardValues:
            if i == deckOrder[53]:
                cardCount = np.where(cardValues == i)[0][0] + 1
                break
            elif i == deckOrder[53] and (i == "JOKa" or i == "JOKb"):
                cardCount = 53
                break
        #Cut the deck by the top card's value while keeping the bottom card at the bottom.
        topDeckCut = []
        bottomDeckCut = []
        bottomCard = deckOrder[53:]

        topDeckCut = deckOrder[0: cardCount]
        bottomDeckCut = deckOrder[cardCount : 53]

        deckOrder = bottomDeckCut + topDeckCut + bottomCard
        
        print(deckOrder) 
        print()

        # Output Line: Count down from the top equal to the cardDict key number of the Top card,
        #              if the card you counted down to is a joker then start the algorithm from
        #              the beginning, if not a joker then that card's cardDict key number is the
        #              output. 
        cardCount = 0 
        for i in cardValues:
            if i == deckOrder[0] and (i != "JOKa" and i != "JOKb"):
                cardCount = np.where(cardValues == i)[0][0] + 1
                break
            elif i == deckOrder[0] and (i == "JOKa" or i == "JOKb"):
                cardCount = np.where(cardValues == i)[0][0] 
        if deckOrder[cardCount] == "JOKa" or deckOrder[cardCount] == "JOKb":
            continue
        outputLine.append(deckOrder[cardCount])
        l += 1

        print("Outputline")
        print(outputLine)
        print()
        
    ###############################################################################################
    #Encryption:
    # If the isEncryptMode parameter is set to True then we run this:
    
    # Add message text num values to outputLine num values (modulo 26).
    # This is now the Cipher texts num values.
    # Convert cipher text num values to letters. This is the Encrypted Cipher Text.
    if isEncryptMode == True:
        print("Encrypt Mode")
        #Convert outputLine to text values and add them to messageNums modulo 26
        outputLineNums = []
        for i in outputLine:
            for k in cardValues:
                if i == k:
                    outputLineNums.append(np.where(cardValues == k)[0][0] + 1)
        #print("MessageNums   ", messageNums)
        #print("OutputLineNums", outputLineNums)

        #Add messageNums to outputLineNums modulo 26 keeping 26 if 26/26 rather than 0
        cipherTextNums = []
        l = 0     
        while l < len(messageNums) and l < len(outputLineNums):
            addedValue = (messageNums[l] + outputLineNums[l])
            addedValue = custom_modulo(addedValue, 26)
            cipherTextNums.append(addedValue)
            l += 1

        #print("cipherTextNums", cipherTextNums)    

        cipherText = []
        #Convert cipherTextNums to cipherText
        for i in cipherTextNums:
            for k in textValues:
                if i == (np.where(textValues == k)[0][0] + 1):
                    cipherText.append(textValues[np.where(textValues == k)[0][0]])
        #print("cipherText", cipherText)

        #Format the Cipher text to be separated by a space for every 5 characters of text.
        l = 0
        cipherTextEncrypted = ""
        cipherTextFormatted = ""
        while l < len(cipherText):
            cipherTextEncrypted += "".join(cipherText[l])
            l += 1      
        cipherTextFormatted = ' '.join(cipherTextEncrypted[i:i+5] for i in range(0, len(cipherTextEncrypted), 5))

        print("Encrypted and Formatted Cipher Text", cipherTextFormatted)
    
    #Decryption
    # If the isEncryptMode parameter is set to decrypt then we run this:
    # Subtract cipher text num values from output text num values (modulo 26).
    # This is now the message text's num values.
    # Convert message text num values to letters. This is the Decrypted Message Text.
    elif isEncryptMode == False:
        print("Decrypt Mode")
        outputLineNums = []
        for i in outputLine:
            for k in cardValues:
                if i == k:
                    outputLineNums.append(np.where(cardValues == k)[0][0] + 1)
                    
        #Subtract messageNums from outputLineNums modulo 26 keeping 26 if 26/26 rather than 0
        cipherTextNums = []
        l = 0     
        while l < len(messageNums) and l < len(outputLineNums):
            subtractedValue = (messageNums[l] - outputLineNums[l])
            subtractedValue = custom_modulo(subtractedValue, 26)
            cipherTextNums.append(subtractedValue)
            l += 1
            
        cipherText = []
        #Convert cipherTextNums to cipherText
        for i in cipherTextNums:
            for k in textValues:
                if i == (np.where(textValues == k)[0][0] + 1):
                    cipherText.append(textValues[np.where(textValues == k)[0][0]])
                    
        #Format the Cipher text to be separated by a space for every 5 characters of text.
        l = 0
        cipherTextDecrypted = ""
        cipherTextFormatted = ""
        while l < len(cipherText):
            cipherTextDecrypted += "".join(cipherText[l])
            l += 1      
        cipherTextFormatted = ' '.join(cipherTextDecrypted[i:i+5] for i in range(0, len(cipherTextDecrypted), 5))

        print("Decrypted and Formatted Cipher Text", cipherTextFormatted)
        
    return deckOrder


# Main function
def main():
    '''
    These Function calls demonstrate the encryption and decryption modes of the Pontifex Cipher.
    The first call is in encrypt mode which encrypts the cipher text "DONOT USEPC" to "HLXMB TKSTJ".
    The second call is in decrypt mode which decypts the cipher text "HLXMB TKSTJ" to "DONOT USEPC".
    '''
    #newOrder = pontifexCipher("DONOT USEPC", True)
    #newOrder = pontifexCipher("HLXMB TKSTJ", False)
    #print(newOrder)
    
    # Do this algorithm for as many characters in the message, and if keyPhrase is default
    # the deck order remains unshuffled, if the keyPhrase is not default then we will
    # permutate the deck according to the keyPhrase letter values, which is a way to shuffle the
    # deck by doing a second count cut using the index of values of the keyPhrase characters.
    
    #Create empty list deck order
    currentDeckOrder = []
    keyPrompt = input("Permute Deck Order by a Key Phrase (Y/N)? \n")
    if keyPrompt.lower() == "y":
        keyPhrase = input("Enter Key Phrase: ")
        currentDeckOrder = pontifexCipher(keyPhrase, True)
        
        modeSelect = input("Encrypt or Decrypt (E/D)?\n")
        if modeSelect.lower() == "e":
            message = input("Enter message to Encrypt: ")
            currentDeckOrder = pontifexCipher(message, True, currentDeckOrder[:])
        elif modeSelect.lower() == "d":
            message = input("Enter message to Decrypt: ")
            currentDeckOrder = pontifexCipher(message, False, currentDeckOrder[:])
    elif keyPrompt.lower() == "n":
        modeSelect = input("Encrypt or Decrypt (E/D)?\n")
        if modeSelect.lower() == "e":
            message = input("Enter message to Encrypt: ")
            currentDeckOrder = pontifexCipher(message, True)
        elif modeSelect.lower() == "d":
            message = input("Enter message to Decrypt: ")
            currentDeckOrder = pontifexCipher(message, False)
    print(currentDeckOrder)
    
# Using the special variable 
# __name__
if __name__=="__main__":
    main()



      
        
