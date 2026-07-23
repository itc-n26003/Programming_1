mountain_in_japan = {'fuji': 3776, 'kitabake': 3193, 'okuhodakadake': 3190, 'dummy': 0}
mountain_in_japan_sorted = sorted(mountain_in_japan.items(), key=lambda x: x[1], reverse=True)
print(mountain_in_japan_sorted)
