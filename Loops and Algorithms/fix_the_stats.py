
# fix_the_stats.py
# Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Logical error: The counter was initialized inside the loop,
# resetting it to 0 on every iteration.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1

print(f"Failed logins: {failed}")

total = 0
count = 0

for value in minutes:
    if value > 0:
        total += value
        count += 1

# Logical error: The print statement was inside the loop,
# causing the average to be printed multiple times.
# Logical error: Integer division (//) was used instead of
# regular division (/), removing the decimal part.
print(f"Average session: {total / count} minutes")

# Logical error: range(1, 4) excludes 4, so the last level
# was missing. Changed the stop value to 5.
for level in range(1, 5):
    print(f"Level {level}")
