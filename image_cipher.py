# Function to encrypt an image using XOR operation
def encrypt_image(input_image_path, output_image_path, key):
    # Open the input image in binary mode
    with open(input_image_path, 'rb') as file:
        image = file.read()  # Read the image file
    
    # Convert the image data to a mutable bytearray
    image = bytearray(image)

    # XOR each byte with the key to encrypt the image
    for i, j in enumerate(image):
        image[i] = j ^ key
    
    # Save the encrypted image to a new file
    with open(output_image_path, 'wb') as file:
        file.write(image)
    print(f"Image encrypted successfully and saved as {output_image_path}")

# Function to decrypt an image using XOR operation
def decrypt_image(input_image_path, output_image_path, key):
    # The decryption process is the same as encryption since XOR is symmetric
    encrypt_image(input_image_path, output_image_path, key)
    print(f"Image decrypted successfully and saved as {output_image_path}")

# Main interactive program
def main():
    print("---------Welcome to Image Cipher Generator----------")
    
    while True:
        try:
            choice = int(input("Encrypt? -> enter '1'\nDecrypt? -> enter '2' \n>> "))
            if choice not in [1, 2]:
                raise ValueError("Invalid choice!")
        except ValueError:
            print("Please enter a valid choice (1 or 2)!")
            continue
        else:
            break

    # Process encryption or decryption based on user input
    if choice == 1:
        img = input("\nEnter the path of the image to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter the key value for encryption (integer): "))
        encrypt_image(img, output_path, key)
    
    elif choice == 2:
        img = input("\nEnter the path of the image to decrypt: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the key value for decryption (integer): "))
        decrypt_image(img, output_path, key)

if __name__ == "__main__":
    main()
