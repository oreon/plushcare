
codes = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}

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

def decode(msg):
    '''
    a method to convert vowels into letters 
    assumes the sentence is already in small case 
    '''
    if msg == None:
        return None
   
    for vowel, code in codes.items():
        msg = msg.replace(code, vowel)

    return msg

if __name__ == "__main__":
    print (codes.items())
    print (codes.keys())
    print ( encode('this is a message') )
    print ( decode('th3s 3s 1 m2ss1g2') )

    print (encode(''))