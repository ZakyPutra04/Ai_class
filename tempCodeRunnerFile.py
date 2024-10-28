x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

# Mencari y1 di dalam x
if y1 in x:
    output_y1 = x.index(y1)
else:
    output_y1 = 0

# Mencari y2 di dalam x
if y2 in x:
    output_y2 = x.index(y2)
else:
    output_y2 = 0

print("Index y1:", output_y1)
print("Index y2:", output_y2)
