decimal = int(input("Please enter an integer"))
bit_size = int(input("Please enter the size of the representation"))

def decimal_to_binary(number,size):
    binary = bin(number)[2:]
    if len(binary)<size:
        binary = binary.zfill(size)
    else:
        binary = binary[-size:]
    return binary

def apply_two_compliment(binary,size):
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
    inverted_decimal = int(inverted,2)+1
    negative_binary = decimal_to_binary(inverted_decimal,size)
    return negative_binary 

binaryDec = decimal_to_binary(decimal,bit_size)
new_decimal = apply_two_compliment(binaryDec,bit_size)
print(new_decimal)