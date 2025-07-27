n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

first = a[0]
second = None

for num in a[1:]:
    if num != first:
        second = num
        break

if second is not None:
    print(second)
else:
    print("No second largest number")
