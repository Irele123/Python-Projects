alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encyrpt(text, shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"    
    if shift >= 1:
        text_list=list(text)
        text_len=len(text_list)
        
        for i in range(0,text_len):
            if text_list[i] not in alphabet:
                text_list[i] = text_list[i]
            
            else:
                encode_index = alphabet.index(text_list[i])
                encode_index = encode_index + shift
            
                if encode_index > 25:
                    encode_index=encode_index-26
                
                text_list[i]=alphabet[encode_index]
        
        seperator=""  
        new_text=seperator.join(text_list)
    
    else:
        new_text=text
        
    return new_text

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decyrpt(text, shift):
    if shift >= 1:
        text_list=list(text)
        text_len=len(text_list)
        
        for i in range(0,text_len):
            if text_list[i] not in alphabet:
                text_list[i] = text_list[i]
            
            else:
                decode_index = alphabet.index(text_list[i])
                decode_index = decode_index - shift  
                
                if decode_index <0:
                    decode_index=26+decode_index
                    
                
                text_list[i]=alphabet[decode_index]
        
        seperator=""  
        new_text=seperator.join(text_list)
            
    else:
        new_text=text
                
    return new_text        
                
                
if direction == "encode":
    print(encyrpt(text, shift))

elif direction == "decode":
        print(decyrpt(text,shift))