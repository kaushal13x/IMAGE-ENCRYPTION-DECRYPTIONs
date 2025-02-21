import cv2
import numpy as np

# Load images
original = cv2.imread("input.png")
encrypted = cv2.imread("encrypted.png")

# Compare both images
difference = cv2.absdiff(original, encrypted)
if np.any(difference):
    print("✅ Encryption Successful! Encrypted image is different from the original.")
else:
    print("❌ Encryption Failed! Images are identical.")

cv2.imshow("Encrypted Image", encrypted)
cv2.waitKey(0)
cv2.destroyAllWindows()
