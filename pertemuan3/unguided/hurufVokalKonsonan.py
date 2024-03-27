userInput = input("Masukan sebuah huruf: ").lower() ## convert ke Lowercase

if (userInput == "a" or userInput == "i" or userInput == "u" or userInput == "e" or userInput == "o"):
    print(f"{userInput} adalah huruf vokal")
else:
    print(f"{userInput} huruf konsonan")
