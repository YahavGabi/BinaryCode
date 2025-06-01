def encrypt_decrypt_xor(filename, key):
    with open(filename,'rb') as file:
        data = file.read()
        encrypted_data = bytes([byte^5 for byte in data])
    
    output_filename = "xor_output.bin"
    with open(output_filename,'wb') as out_file:
     out_file.write(encrypted_data)
    print(f"Encrypted file saved as: {output_filename}")

if __name__ == "__main__":
    filename = input("Enter File Name: ")
    key = 5 # המפתח להצפנה/פענוח
    encrypt_decrypt_xor(filename, key)
    
