from CaesarCipherApp import CaesarCipherApp

if __name__ == "__main__":
    ALPHABET_PATH = "alphabet.json"
    app = CaesarCipherApp(ALPHABET_PATH)
    app.mainloop()
