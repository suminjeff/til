def solution(wallpaper):
    row = []
    col = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                row.append(i)
                col.append(j)
    answer = [min(row), min(col), max(row)+1, max(col)+1]

    return answer


wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))
wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper))
wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
print(solution(wallpaper))
wallpaper = ["..", "#."]
print(solution(wallpaper))
