📌 Simple Image Encryption Tool (Python + Tkinter)

This project is a beginner-friendly image encryption and decryption tool built using Python, Tkinter, and Pillow (PIL).
It uses XOR-based pixel manipulation to encrypt and decrypt image files, providing a simple demonstration of how basic image encryption works.

The tool features a Graphical User Interface (GUI) that allows users to:

Select an input image

Choose the output location

Enter an encryption key

Encrypt or decrypt images with a single click

It is designed for educational purposes, especially for students learning about cybersecurity, cryptography, and image processing.

🚀 Features
✔ Simple and Beginner-Friendly

No command-line usage. Everything is done through an intuitive GUI.

✔ GUI Built With Tkinter

Buttons, file pickers, labels, and message boxes for ease of use.

✔ XOR-Based Encryption Algorithm

Performs pixel-level manipulation:

Each pixel’s RGB values are XORed with a key (0–255).

XOR encryption is reversible:
Encrypt → Decrypt using the same key.

✔ Image Format Support

The tool supports:

.png

.jpg

.jpeg

.bmp

✔ Error Handling Included

Invalid key (non-integer or out of range)

Missing input image

Unsupported file type

Unexpected runtime errors

✔ Custom UI Theme

The interface uses a maroon background for visual appeal.
🖼 GUI Preview (Add Screenshot)

(Insert a screenshot here once you run the app and take a picture)
Example filename:screenshots/main_window.png

📦 Requirements

Make sure you have Python and Pillow installed.
Install dependencies:pip install pillow.
Tkinter comes pre-installed with most Python distributions.
if not, install using:pip install tkinter.

🔧 How to Run
Save the script as:image_encrypt_gui.py
Run the file:python3 image_encrypt_gui.py
The GUI window will appear.

📝 How to Use the Application
🔹 1. Select Input Image
Click Browse next to Input Image Path and choose any supported image.

🔹 2. Choose Output Location
Click Browse next to Output Image Path and specify where the processed image will be saved.

🔹 3. Enter Encryption Key
Provide a key between 0 and 255.
Example: 55

🔹 4. Choose an Operation
Click Encrypt to encrypt the image
Click Decrypt to reverse a previously encrypted image

🔹 5. Success or Error Messages
A popup will notify you whether the operation succeeded or failed.

🔐 How the Encryption Works
This tool uses a simple XOR (Exclusive OR) operation on each pixel:

📌 Formula:encrypted_value = original_value XOR key
This is applied to each color channel:
R, G, and B.

📌 Why XOR?

It is reversible using the same key:decrypted_value = encrypted_value XOR key
Fast and easy to implement

Widely used in cryptography as a foundational concept

⚠ Note:

This encryption method is NOT secure for real applications.
It is purely for learning purposes, demonstrating image manipulation and simple encryption.

⚠️ Ethical Use Disclaimer

This project is for educational and experimental purposes only.
Do NOT use it for illegal activities or to obscure images without proper authorization.

The author is not responsible for misuse.
🛠 Code Structure Overview
|-- encrypt_image()      # Encrypts image using XOR
|-- decrypt_image()      # Decrypts encrypted image using XOR
|-- browse_input()       # File dialog for input image
|-- browse_output()      # File dialog for output path
|-- handle_encrypt()     # Triggers encryption from GUI button
|-- handle_decrypt()     # Triggers decryption from GUI button
|-- Tkinter GUI setup    # Window configuration, labels, entries, buttons

💡 Common Issues & Fixes
❌ “Invalid Key” Error
Your key must be a number between 0–255.

❌ “Input file not found”
The path does not exist or you did not select a file.

❌ “Unexpected Error”
This may happen if the image type is corrupted or unsupported.

📘 Possible Improvements (Future Enhancements)
Add AES encryption (real cryptography)
Add image preview before/after encryption
Add theme customization
Add drag-and-drop functionality
Convert project to a standalone .exe or .apk

📄 License
This project is released under the MIT License.
You may freely modify and use it for learning or projects.

🙌 Author
IDU SAMUEL
Cybersecurity & Programming Enthusiast
