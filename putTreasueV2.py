row1 = ["X","X","X"]
row2 = ["X","X","X"]
row3 = ["X","X","X"]

map = [row1,row2,row3]
print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")
Position = input("Where do you wanna put the treasue? (row and colomn eg. 23): ")
map[int(Position[0])-1][int(Position[1])-1] = "O"
print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")
