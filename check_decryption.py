import cv2
import numpy as np

# Load images
original = cv2.imread("input.png")
decrypted = cv2.imread("decrypted.png")

# Compare both images
difference = cv2.absdiff(original, decrypted)
if not np.any(difference):
    print("✅ Decryption Successful! Image is identical to the original.")
else:
    print("❌ Decryption Failed! Images are different.")

cv2.imshow("Decrypted Image", decrypted)
cv2.waitKey(0)
cv2.destroyAllWindows()
