# session_timer.py - Converts seconds into minutes and remaining seconds.
seconds = int(input("enter the number of seconds : "))

mn = seconds//60
sec = seconds%60

print(f"minutes : {mn} ,seconds {sec}")

# enter the number of seconds : 905
# minutes : 15 ,seconds 5
# enter the number of seconds : 60
# minutes : 1 ,seconds 0
# enter the number of seconds : 59
# minutes : 0 ,seconds 59