row1 = ["X","X","X"]
row2 = ["X","X","X"]
row3 = ["X","X","X"]

map = [row1,row2,row3]
print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")
rowPosition = int(input("Where do you wanna put the treasure? (row): (1,2,3): "))-1
colPosition = int(input("Where do you wanna put the treasure? (column): (1,2,3): "))-1
map[rowPosition][colPosition] = "O"
print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")
