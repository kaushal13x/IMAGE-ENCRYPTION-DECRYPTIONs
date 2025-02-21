🔒 Image Encryption & Decryption
A Python project for encrypting and decrypting images using OpenCV. Secure your images with pixel shuffling & XOR-based encryption.

🚀 Features
✅ Encrypts and decrypts images securely
✅ Uses pixel shuffling + XOR encryption
✅ Supports PNG, JPG, and other formats
✅ Simple command-line execution

🔧 Setup & Installation
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/kaushal13x/IMAGE-ENCRYPTION-DECRYPTION.git
cd IMAGE-ENCRYPTION-DECRYPTION
2️⃣ Create a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv .venv
3️⃣ Activate the Virtual Environment
➤ On Windows:
bash
Copy
Edit
.venv\Scripts\activate
➤ On macOS/Linux:
bash
Copy
Edit
source .venv/bin/activate
4️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5️⃣ Run the Script
To encrypt/decrypt images, run:

bash
Copy
Edit
python script.py
📌 How It Works?
🔹 Encryption: The script shuffles pixels and applies XOR encryption.
🔹 Decryption: The script reverses the process to get back the original image.

📷 Example Usage
python
Copy
Edit
from encryptor import encrypt_image, decrypt_image

encrypt_image("input.png", key=12345)
decrypt_image("encrypted.png", key=12345)
📜 License
This project is open-source and free to use.

📩 Contributing
Pull requests are welcome! Feel free to contribute. isako sidha paste kr du ky
