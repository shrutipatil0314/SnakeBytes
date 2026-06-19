# || User defined functions  ||

def greeting_someone(name):
    print(f"Hello, {name}! How are you today?")
    print("I hope you're having a great day!")

#calling the function
greeting_someone("Alice")
greeting_someone("Bob")
greeting_someone("Charlie")


#example 2
def even_or_odd(number):
    if number % 2 == 0:
        print("is an even number.")
    else:
        print("is ot an even number.")


even_or_odd(4)
even_or_odd(7)
