import qrcode

def main():
    img = qrcode.make('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    type(img) # qrcode.image.pil.PilImage
    img.save("./assets/not_rick_roll.png")

if __name__ == "__main__":
    main()
