from random import choice
from time import sleep

class GreenlightRedlight:
    def __init__(self):
        self.moves = 0
        self.maxmoves = 5

    def startgame(self):
        print("Welcome to Green Light, Red Light")
        print("Type 'move' when it's Green Light, but stay still (type Enter key) if you see Red Light")
        print("Type 'exit' to quit.")

        while self.moves < self.maxmoves:
            getlight = choice(["Red Light", "Green Light"])
            print(f"{getlight}")

            sleep(2) # Timer for each light

            if getlight == "Green Light":
                # sleep(2) # Timer, 2 = 2 seconds

                playeraction = input("Your action : ").lower()

                if playeraction == "move":
                    self.moves += 1
                    print(f"Good Job! Moves: {self.moves}/{self.maxmoves}")
                elif playeraction == "exit":
                    print("Thanks for playing!")
                    break
                else:
                    print("Game Over!!!, You missed the Green Light.")
                    break
                
            elif getlight == "Red Light":
                # sleep(2) # Timer, 2 = 2 seconds

                print("Red Light! Don't Move!")
                playeraction = input("Your action : ").lower()
                
                if playeraction == "move":
                    print("Game Over!!!, You moved on Red Light.")
                    break
                elif playeraction == "exit":
                    print("Thanks for playing!")
                    break

        if self.moves >= self.maxmoves:
            print("Congratulations! You Won")      


def main():
    game: GreenlightRedlight = GreenlightRedlight()
    game.startgame()

if __name__ == "__main__":
    main()

# gmail