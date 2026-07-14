import qrcode

# 🌟 PASTE your active lhr.life link from your SSH terminal inside the quotes below!
web_link = "https://422dea870ab789.lhr.life" 

# Generate the QR Code matrix
qr_image = qrcode.make(web_link)

# Save it as an image file
qr_image.save("cafe_qr.png")

print(f"🎉 Success! 'cafe_qr.png' created pointing to {web_link}")