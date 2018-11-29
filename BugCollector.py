# Benjamin Readman
# Bug Collector
numBug = int(input("Please enter the number of bugs" +
" collected on the first day: "))
print("Okay, thank you.")
x = 0 
while x < 4:
    nextBug = int(input("How about the next day: "))
    print()
    numBug += nextBug
    x += 1
print("You collected a total of",numBug,"bugs over 5 days.")