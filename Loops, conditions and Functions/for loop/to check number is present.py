num=[1,2,3,4,5,6]
n=3
found=False
for nums in num:
    if nums == n:
        found=True
        break
print(f'List contains {n}: {found}')