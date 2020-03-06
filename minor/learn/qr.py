import qrcode

img=qrcode.make('ankit'+' '+'210')

print(type(img))

img.save('qr.png')
