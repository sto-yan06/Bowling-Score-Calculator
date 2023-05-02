frames_scores = []
current_frame = 1
current_roll = 1
total_score = 0

while current_frame <= 10:

    pins = int(input("Enter the number of pins knocked down on roll " + str(current_roll) + " of frame " + str(current_frame) + ": "))

    total_score += pins

    if current_roll == 2 or pins == 10:

        if current_roll == 1 and pins == 10:
            next_pins_strike_1 = int(
                input("You hit a Strike, Enter the number of pins knocked down on the first roll: "))
            total_score += next_pins_strike_1
            if next_pins_strike_1 == 10:
                total_score += 10
            else:
                next_pins_strike_2 = int(
                    input("You hit a Strike, Enter the number of pins knocked down on the second roll: "))
                total_score += next_pins_strike_2

        if current_roll == 1 and len(frames_scores) > 0 and frames_scores[-1] == 10:
            total_score += pins
            if current_frame == 10 and pins == 10:
                bonus_pins_1 = int(input("You hit a Strike on tenth one! Roll two more: "))
                total_score += bonus_pins_1
                bonus_pins_2 = int(input("You hit a Strike on tenth frame! Roll one more: "))
                total_score += bonus_pins_2

        elif current_roll == 2 and total_score == 10:
            if current_frame < 10:
                next_pins_spare = int(input("You hit a Spare, Enter the number of pins knocked down on the next roll: "))
                total_score += next_pins_spare
            else:
                bonus_pins = int(input("You hit a Spare on tenth frame! Roll one more: "))
                total_score += bonus_pins
        frames_scores.append(total_score)
        print("Score after frame " + str(current_frame) + ": " + str(sum(frames_scores)))
        total_score = 0
        current_frame += 1
        current_roll = 1

    else:
        current_roll += 1


print("Final score: " + str(sum(frames_scores)))
