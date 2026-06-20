import qrcode

# Get input from the user
data = input("Enter text or URL: ")

# Create QR code
qr = qrcode.make(data)

# Save the image
qr.save("qrcode.png")

print("QR Code generated successfully!")
print("Saved as qrcode.png")