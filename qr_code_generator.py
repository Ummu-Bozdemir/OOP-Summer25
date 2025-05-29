import qrcode

url = "https://ummu-warsaw-website-project.lovable.app/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("ummu_website_qr.png")

print("QR code generated and saved as 'ummu_website_qr.png'")
