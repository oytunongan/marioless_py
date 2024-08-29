# TODO
while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        print("Wrong input")

for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
