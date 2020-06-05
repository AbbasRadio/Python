def encode(str,getCode):
    newStr=''
    for i in str:
        getLetter = ord(i)+getCode-105
        newStr +=chr(getLetter)
        # print(newStr,end="")
    return newStr
def decode(newStr,getCode):
    oldStr=''
    for i in newStr:
        setLetter = ord(i)-getCode+105
        oldStr += chr(setLetter)
    return oldStr
str = input("Enter Your Message Which You Want to Encode : ")
AskChange = input("Enter Letter to Encode it With : ")
getCode = ord(AskChange)
encodedMsg = encode(str,getCode)
print(encodedMsg)
print(decode(encodedMsg,getCode))