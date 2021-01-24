row_1 = ["⬜️","️⬜️","️⬜️"]
row_2 = ["⬜️","⬜️","️⬜️"]
row_3 = ["⬜️","⬜️️","⬜️️"]

map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

print("Example Position: Column 1, Row 2 = 12")
input_position = input("Where do you want to put the treasure? ")

horizontal = int(input_position[0])
vertical = int(input_position[1])

map[vertical - 1][horizontal - 1] = " X"

print(f" {row_1}\n {row_2}\n {row_3}")

print("You have successfully hidden your treasure!")
