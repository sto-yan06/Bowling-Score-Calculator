import random

def choose_game_mode():
    game = BowlingGame()

    mode = input("Choose a game mode (1 - Auto, 2 - Manual): ")

    if mode == '1':
        game.play_game_auto()
    elif mode == '2':
        game.play_game_manual()
    else:
        print("Invalid game mode selection. Please choose 1 or 2.")
        choose_game_mode()

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() == "Y":
        choose_game_mode()

class BowlingGame:
    def __init__(self):
        self.frames_scores = []
        self.current_frame = 1
        self.current_roll = 1
        self.total_score = 0

    def play_game_auto(self):
        while self.current_frame <= 10:
            pins = random.randint(0, 10)
            self.total_score += pins

            if self.current_roll == 2 or pins == 10:
                if self.current_roll == 1 and pins == 10:
                    next_pins_strike_1 = random.randint(0, 10)
                    self.total_score += next_pins_strike_1
                    if next_pins_strike_1 == 10:
                        self.total_score += 10
                    else:
                        next_pins_strike_2 = random.randint(0, 10)
                        self.total_score += next_pins_strike_2

                if self.current_roll == 1 and len(self.frames_scores) > 0 and self.frames_scores[-1] == 10:
                    self.total_score += pins
                    if self.current_frame == 10 and pins == 10:
                        bonus_pins_1 = random.randint(0, 10)
                        self.total_score += bonus_pins_1
                        bonus_pins_2 = random.randint(0, 10)
                        self.total_score += bonus_pins_2

                elif self.current_roll == 2 and self.total_score == 10:
                    if self.current_frame < 10:
                        next_pins_spare = random.randint(0, 10)
                        self.total_score += next_pins_spare
                    else:
                        bonus_pins = random.randint(0, 10)
                        self.total_score += bonus_pins

                self.frames_scores.append(self.total_score)
                print("Score after frame " + str(self.current_frame) + ": " + str(sum(self.frames_scores)))
                self.total_score = 0
                self.current_frame += 1
                self.current_roll = 1
            else:
                self.current_roll += 1

        print("Final score: " + str(sum(self.frames_scores)))
        return int(sum(self.frames_scores))

    def play_game_manual(self):
        while self.current_frame <= 10:
            pins = int(input(
                "Enter the number of pins knocked down on roll " + str(self.current_roll) + " of frame " + str(
                    self.current_frame) + ": "))
            self.total_score += pins

            if self.current_roll == 2 or pins == 10:
                if self.current_roll == 1 and pins == 10:
                    next_pins_strike_1 = int(
                        input("You hit a Strike, Enter the number of pins knocked down on the first roll: "))
                    self.total_score += next_pins_strike_1
                    if next_pins_strike_1 == 10:
                        self.total_score += 10
                    else:
                        next_pins_strike_2 = int(
                            input("You hit a Strike, Enter the number of pins knocked down on the second roll: "))
                        self.total_score += next_pins_strike_2

                if self.current_roll == 1 and len(self.frames_scores) > 0 and self.frames_scores[-1] == 10:
                    self.total_score += pins
                    if self.current_frame == 10 and pins == 10:
                        bonus_pins_1 = int(input("You hit a Strike on tenth one! Roll two more: "))
                        self.total_score += bonus_pins_1
                        bonus_pins_2 = int(input("You hit a Strike on tenth frame! Roll one more: "))
                        self.total_score += bonus_pins_2

                elif self.current_roll == 2 and self.total_score == 10:
                    if self.current_frame < 10:
                        next_pins_spare = int(
                            input("You hit a Spare, Enter the number of pins knocked down on the next roll: "))
                        self.total_score += next_pins_spare
                    else:
                        bonus_pins = int(input("You hit a Spare on tenth frame! Roll one more: "))
                        self.total_score += bonus_pins

                self.frames_scores.append(self.total_score)
                print("Score after frame " + str(self.current_frame) + ": " + str(sum(self.frames_scores)))
                self.total_score = 0
                self.current_frame += 1
                self.current_roll = 1
            else:
                self.current_roll += 1

        print("Final score: " + str(sum(self.frames_scores)))
        return int(sum(self.frames_scores))
