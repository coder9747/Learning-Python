import qrcode

def make_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    file_name = input("Enter File Name")
    img.save(f"{file_name}.png");


text = input("Enter The Text");
make_qr_code(text=text);