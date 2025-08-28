print('Project -  Crypto')
def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
# create two dictionaries
    encrypt = dict(zip(keys,values))
    decrypt = dict(zip(values,keys))

#user input 'the message' and mode
    msg = input(f"Enter the message : ")
    mode = input(f"enter the mode e for encryption and d for decryption : ")

# run encode or decode
    if mode.lower() == 'e':
      new_msg = ''.join([encrypt[letter] for letter in msg.lower() ])
    else:
      new_msg = ''.join([decrypt[letter] for letter in msg.lower() ])
    
# return result
    return new_msg
# clean and beautify the code 

print(enigma_light())