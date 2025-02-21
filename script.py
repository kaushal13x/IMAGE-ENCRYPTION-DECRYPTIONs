import cv2
import numpy as np
import random

def encrypt_image(image_path, key):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise ValueError("Image not found or unsupported format.")
    
    encrypted_image = image.copy()
    height, width, channels = image.shape
    random.seed(key)
    
    # Shuffle pixel positions
    indices = [(x, y) for x in range(width) for y in range(height)]
    random.shuffle(indices)
    
    shuffled_image = np.zeros_like(encrypted_image)
    for i, (x, y) in enumerate(indices):
        new_x, new_y = divmod(i, height)
        shuffled_image[new_y, new_x] = encrypted_image[y, x]
    
    # Apply XOR operation
    xor_key = np.full_like(shuffled_image, key % 256, dtype=np.uint8)
    shuffled_image = cv2.bitwise_xor(shuffled_image, xor_key)
    
    cv2.imwrite("encrypted.png", shuffled_image)
    print("Encryption complete. Image saved as 'encrypted.png'")
    return shuffled_image

def decrypt_image(encrypted_path, key):
    encrypted_image = cv2.imread(encrypted_path, cv2.IMREAD_UNCHANGED)
    if encrypted_image is None:
        raise ValueError("Encrypted image not found or unsupported format.")
    
    decrypted_image = encrypted_image.copy()
    height, width, channels = encrypted_image.shape
    random.seed(key)
    
    # Reverse XOR operation
    xor_key = np.full_like(decrypted_image, key % 256, dtype=np.uint8)
    decrypted_image = cv2.bitwise_xor(decrypted_image, xor_key)
    
    # Reverse pixel shuffling
    indices = [(x, y) for x in range(width) for y in range(height)]
    random.shuffle(indices)
    
    original_image = np.zeros_like(decrypted_image)
    for i, (x, y) in enumerate(indices):
        new_x, new_y = divmod(i, height)
        original_image[y, x] = decrypted_image[new_y, new_x]
    
    cv2.imwrite("decrypted.png", original_image)
    print("Decryption complete. Image saved as 'decrypted.png'")
    return original_image

# Example usage
if __name__ == "__main__":
    key = 12345  # Key for encryption and decryption
    encrypt_image("input.png", key)
    decrypt_image("encrypted.png", key)
