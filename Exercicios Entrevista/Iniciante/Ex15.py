# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

nameComplete = []


def complete(comp):
    reversed(comp)
    for letters in comp:
        nameComplete.append(letters)
    return nameComplete


name = input("Nome:\n")
lastName = input("Sobrenome:\n")

complete(name)
complete(lastName)

print(nameComplete)
