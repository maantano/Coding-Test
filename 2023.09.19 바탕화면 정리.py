wallpaper = [".#...", "..#..", "...#."]
# wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
result = [0, 1, 3, 4]

def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                a.append(i)
                b.append(j)
    print([min(a), min(b), max(a) + 1, max(b) + 1])
    return [min(a), min(b), max(a) + 1, max(b) + 1]


solution(wallpaper)
