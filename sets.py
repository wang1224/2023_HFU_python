set_1 = set([1, 2, 3, 5, 5, 6, 6])
set_2 = set([4, 4, 4, 5, 5, 6, 6])

print(set_1, set_2)
print(f"Intersection(1): {set_1.intersection(set_2)}")
print(f"Intersection(2): {set.intersection(set_1, set_2)}")

print(f"Union(1): {set_1.union(set_2)}")
print(f"Union(2): {set.union(set_1, set_2)}")

print(f"Diff (1->2): {set_1.difference(set_2)}")
print(f"Diff (2->1): {set_2.difference(set_1)}")

# set_1.symmetric_difference(set_2)
# set.symmetric_difference(set_1, set_2)