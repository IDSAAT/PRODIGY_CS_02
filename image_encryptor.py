import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


def encrypt_image(input_path, output_path, key):
    try:
        key = int(key)
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Key", "Key must be a number between 0 and 255.")
        return

    try:
        img = Image.open(input_path)
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        messagebox.showinfo("Success", "Image successfully encrypted and saved!")
    except FileNotFoundError:
        messagebox.showerror("Error", "Input image file not found.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))


def decrypt_image(input_path, output_path, key):
    try:
        key = int(key)
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Key", "Key must be a number between 0 and 255.")
        return

    try:
        img = Image.open(input_path)
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        messagebox.showinfo("Success", "Image successfully decrypted and saved!")
    except FileNotFoundError:
        messagebox.showerror("Error", "Encrypted image not found.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))


# ------------------------
# GUI Setup
# ------------------------

def browse_input():
    filename = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    input_entry.delete(0, tk.END)
    input_entry.insert(0, filename)


def browse_output():
    filename = filedialog.asksaveasfilename(
        title="Save output image",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg")]
    )
    output_entry.delete(0, tk.END)
    output_entry.insert(0, filename)


def handle_encrypt():
    encrypt_image(input_entry.get(), output_entry.get(), key_entry.get())


def handle_decrypt():
    decrypt_image(input_entry.get(), output_entry.get(), key_entry.get())


# Main window
root = tk.Tk()
root.title("Simple Image Encryption Tool")
root.geometry("450x300")
root.resizable(True, True)

# Set maroon background
root.configure(bg="#800000")

# ------------ Widgets ------------
label_style = {"bg": "#800000", "fg": "grey", "font": ("Arial", 10, "bold")}

tk.Label(root, text="Input Image Path:", **label_style).pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()
tk.Button(root, text="Browse", command=browse_input).pack()

tk.Label(root, text="Output Image Path:", **label_style).pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
tk.Button(root, text="Browse", command=browse_output).pack()

tk.Label(root, text="Key (0–255):", **label_style).pack()
key_entry = tk.Entry(root, width=20)
key_entry.pack()

tk.Button(root, text="Encrypt", width=40, command=handle_encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", width=40, command=handle_decrypt).pack()

root.mainloop()