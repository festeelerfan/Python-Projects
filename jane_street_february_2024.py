from random import uniform
from math import sqrt

# Choose a random point inside a square
def random_point_within_square(side_length):
    x = random.uniform(0, side_length)
    y = random.uniform(0, side_length)
    return x, y

# Find the midpoint of our chosen points
def midpoint(point1, point2):
  return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

# Determine whether the circle formed by the two points crosses over our [0, side_length]**2 square
def circle_outside_boundaries(point1, point2, side_length):
    r = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) / 2
    mid = midpoint(point1, point2)
    if max(mid[0] + r, mid[1] + r) > side_length or min(mid[0] - r, mid[1] - r) < 0:
      return True # Consider imagining our circle incribed in a square to understand why the above critera are sufficient
    return False


side_length = 1
num_experiments = 100000000
outside_count = 0

for _ in range(num_experiments):
    point1 = random_point_within_square(side_length)
    point2 = random_point_within_square(side_length)

    if circle_outside_boundaries(point1, point2, side_length):
        outside_count += 1

proportion_outside = outside_count / num_experiments

print(f"Proportion of circles outside the boundaries: {proportion_outside}")

vals = [0.47642928, 0.47643562, 0.47632693, 0.47636514, 0.47644894, 0.4763266, 0.47644982, 0.47637184, 0.47639338, 0.47644307]
sum(vals)/len(vals)
