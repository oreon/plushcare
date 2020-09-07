

def encode(msg):
    '''
    a method to convert vowels into letters 
    assumes the sentence is already in small case 
    '''
    if msg == None:
        return None
    codes = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    for vowel, code in codes.items():
        msg = msg.replace(vowel, code)

    return msg

if __name__ == "__main__":
    print ( encode('this is a message') )
    print (encode(''))