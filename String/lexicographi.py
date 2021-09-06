def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('Exabyting123'))
print(lexicographi_sort('last2words'))
