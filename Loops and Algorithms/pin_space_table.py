
# pin_space_table.py
# Calculate the time needed to guess every PIN from 4 to 8 digits.

GUESSES_PER_SECOND = 10

for digit in range(4, 9):
    times = 10 ** digit
    seconds = times // GUESSES_PER_SECOND
    days = seconds // (24 * 60 * 60)
    minutes = seconds // 60
    print(f"{digit} digits: {times} PINs, {minutes} minutes, {days} days")
