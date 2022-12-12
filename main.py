class Character:
    def __init__(self, name, phrase1, phrase2, level):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2 
        self.level = level

    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        if phraseNum == 2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel

kungfupanda = Character("Kung Fu Panda", "Skadoosh", "You have been blinded by pure awesomeness!", 0)
spiderman = Character("Spiderman", "My Spider-Sense is tingling", "Your friendly neighbourhood spiderman.", 0)

kungfupanda.speak(1)
spiderman.setLevel(2)
spiderman.speak(2)