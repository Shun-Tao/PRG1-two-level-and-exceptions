scores = [[78, 81, 84],
          [55, 54, 62],
          [89, 71, 90],
          [99,100]]

print(scores[1][2])
print(scores[2][1])

print(scores[1])

print(len(scores))
print(len(scores[0]))

print("---")

for row in scores:
    print(row)

print("---")

for row in scores:
    for mark in row:
        print(mark)

print("---")

for row in scores:
    print(row[0])


print("---")

total = 0
for row in scores:
    total += row[1]

print(total)


print("---")

print(sum(scores[1]))