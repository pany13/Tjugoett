import os
import random #Importera funktionen "random" för att slumpa dragningen senare

class Tjugoett: #En klass   
    def __init__(self):
        # Listor att lagra korten / poängen i.
        self.player_cards = []  #Användarens kort 
        self.computer_cards = []  #Datorns kort

    def draw_card(self): #En metod
        card = random.randint(1, 11) #Slumpar fram kort mellan 1 och 11
        if card == 1: #Om random blir en 1a så tolkas det som ett Ess vars värde då slumpas till antingen 1 eller 14
            card = random.choice([1, 14])
        return card

    def spela(self):
        os.system('cls' if os.name == 'nt' else 'clear') #Rensa skärmen
        #Första dragningen sker redan här, värdena läggs till listorna som skapades på rad 6-7
        self.player_cards.append(self.draw_card())
        self.computer_cards.append(self.draw_card())

        while True:
            print("\nVi tar en runda av TJUGOETT!")
            print("-" * 28)
            print("\nSpelarens dragna kort:", self.player_cards) #Visa kortet som spelaren drog genom att visa innehållet i listan.
            print("Spelarens poäng:", sum(self.player_cards)) #Visa spelarens totala poäng.
            #Avsluta om spelaren kommer över 21
            if sum(self.player_cards) > 21:
                print("Spelaren är över 21! Spelaren förlorade!")
                break
            player_choice = input("Vill du dra ytterligare ett kort? (ja / nej): ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')
        
            if player_choice == "ja":
                self.player_cards.append(self.draw_card())
            elif player_choice == "nej":
                break
            else:
                print("Fel! Skriv 'ja' eller 'nej'.")

        #Datorns tur, fortsätter dra kort sålänge den är under 21 poäng
        while sum(self.computer_cards) < 21:
            self.computer_cards.append(self.draw_card())

        #Summera poängen i listorna från rad 6-7 och lägg till i variabler
        player_total = sum(self.player_cards)
        computer_total = sum(self.computer_cards)

        #Summera utfallet av rundan
        print("\nDatorns dragna kort:", self.computer_cards)
        print("Datorns poäng:", sum(self.computer_cards)) #Visa datorns totala poäng.
        print("Spelarens poäng:", sum(self.player_cards)) #Visa spelarens totala poäng.
        
        if player_total > 21 or (computer_total <= 21 and computer_total >= player_total): #Datorn vinner baserat på villkoren
            print("Datorn vann!")
        elif computer_total > 21 or (player_total <= 21 and player_total > computer_total): #Spelaren vinner baserat på villkoren
            print("Spelaren vann!")
        else:
            print("Datorn vann! (Det blev oavgjort!)")

if __name__ == "__main__":
    game = Tjugoett()
    game.spela()
