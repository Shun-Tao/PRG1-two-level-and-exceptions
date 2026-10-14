"""
Reading a file that is not perfect

Yesterday's rainfall reader, given a file with two bad lines in it.
This version already copes. Your job is to work out how, and to
decide whether coping is the right thing to do.
"""

WET_THRESHOLD = 100

with open("rainfall.txt", "r") as f:
    lines = f.readlines()

total = 0
count = 0
rejected = []

for line in lines:
    try:     
        station, millimetres_text = line.strip().split(",")

        millimetres = int(millimetres_text)
    except ValueError as problem:
        rejected.append(f"{line.strip()}  ({problem})")
        continue

    total = total + millimetres
    count = count + 1
    status = "Wet" if millimetres >= WET_THRESHOLD else "Dry"
    print(f"{station}: {millimetres} mm ({status})")

print("---")
print(f"{count} stations read, {len(rejected)} rejected")
print(f"Average of the readings that worked: {total / count:.1f} mm")

if rejected:
    print("Rejected lines:")
    for line in rejected:
        print(f"  {line}")

    with open("rejected.txt","w") as f:
        for line in rejected:
            f.write(line+"\n")

if len(rejected) > len(lines)/5:
    raise ValueError("Too many invalid records")
