import qrcode
# img = qrcode.make('Some data here')
# type(img) # qrcode.image.pil.PilImage
# img.save("some_file.png")

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename (include .jpg or .png): ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')