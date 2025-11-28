total = 0
for i in range(1, 101):
    total += i
print(total)

print("1到100的和是:", sum(range(1, 101)))

for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}', end='\t')
    print()
# The only difference is the indentation of the for loop inside the for loop.
