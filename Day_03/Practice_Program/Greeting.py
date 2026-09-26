
def decorator(func):
    def wrapper (msg):
        func(msg.upper())
    return wrapper

@decorator
def display_greeting(msg):
    print(msg)

if __name__ == "__main__":
    display_greeting("Good Morning EveryOne !!")
