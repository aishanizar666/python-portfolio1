
# log_analyzer.py
# Analyze authentication logs and report suspicious activity.

ALERT_LIMIT = 3

LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""


def get_field(line, name):
    """Return the value after name=, or an empty string."""
    start = line.find(name + '=')

    if start == -1:
        return ""

    start += len(name) + 1
    end = start

    while end < len(line) and line[end] != ' ':
        end += 1

    return line[start:end]


def get_status(line):
    """Return the status from a log line."""
    x = line.split()
    return x[1]


def count_status(status):
    """Count log lines with the given status."""
    cnt = 0
    x = LOG.splitlines()

    for line in x:
        if get_status(line) == status:
            cnt += 1

    return cnt


def show_summary():
    """Print the total, failed, and successful login counts."""
    print(f"Lines: {len(LOG.splitlines())}")
    print(f"Failed: {count_status('FAILED')}")
    print(f"OK: {count_status('OK')}")


def search(keyword):
    """Print matching log lines and their line numbers."""
    x = LOG.splitlines()
    matches = 0
    cnt = 1

    for line in x:
        newline = line.lower()

        if newline.find(keyword.lower()) != -1:
            print(f"{cnt}: {line}")
            matches += 1

        cnt += 1

    print(f"Matches: {matches}")


def ip_report(ip):
    """Report failed logins from an IP and warn if the limit is reached."""
    failed = 0
    x = LOG.splitlines()

    for line in x:
        if get_field(line, "ip") == ip and get_status(line) == "FAILED":
            failed += 1
            print(line.split()[0] + ' ' + get_field(line, 'user'))

    print(f"Failed logins from {ip}: {failed}")

    if failed >= ALERT_LIMIT:
        print("ALERT: possible password guessing.")


def mask(word):
    """Hide the middle characters of a word using stars."""
    stars = len(word) - 2
    ans = ""

    if len(word) > 2:
        ans = word[0] + '*' * stars + word[-1]
    else:
        ans = len(word) * "*"

    return ans


def show_masked():
    """Print log lines with usernames masked."""
    x = LOG.splitlines()

    for line in x:
        user = get_field(line, "user")
        line = line.replace("user=" + user, "user=" + mask(user))
        print(line)


def show_menu():
    """Display the analyzer menu."""
    print("""AUTH LOG ANALYZER
1. Summary
2. Search
3. IP report
4. Masked log
q. Quit""")


show_menu()

while True:
    choice = input("Choice: ").strip().lower()

    if choice == '1':
        show_summary()

    elif choice == '2':
        keyword = input("Keyword: ")
        search(keyword)

    elif choice == '3':
        ip = input("IP: ")
        ip_report(ip)

    elif choice == '4':
        show_masked()

    elif choice == 'q':
        print("Bye.")
        break

    else:
        print("Unknown choice.")
