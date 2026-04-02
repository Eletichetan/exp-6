# Bayesian Network (Manual Implementation)

# Dataset
data = [
    {'Rain': 0, 'Sprinkler': 0, 'WetGrass': 0},
    {'Rain': 0, 'Sprinkler': 1, 'WetGrass': 1},
    {'Rain': 1, 'Sprinkler': 0, 'WetGrass': 1},
    {'Rain': 1, 'Sprinkler': 1, 'WetGrass': 1},
    {'Rain': 0, 'Sprinkler': 0, 'WetGrass': 0},
    {'Rain': 1, 'Sprinkler': 0, 'WetGrass': 1},
    {'Rain': 0, 'Sprinkler': 1, 'WetGrass': 1},
    {'Rain': 1, 'Sprinkler': 1, 'WetGrass': 1}
]

# -----------------------------
# Step 1: Count probabilities
# -----------------------------
def probability(var, value, given=None):
    count = 0
    total = 0

    for row in data:
        if given is None or all(row[k] == v for k, v in given.items()):
            total += 1
            if row[var] == value:
                count += 1

    return count / total if total != 0 else 0

# -----------------------------
# Step 2: Basic Probabilities
# -----------------------------
print("P(Rain=1):", probability('Rain', 1))
print("P(Sprinkler=1):", probability('Sprinkler', 1))
print("P(WetGrass=1):", probability('WetGrass', 1))

# -----------------------------
# Step 3: Conditional Probability
# -----------------------------
print("\nP(Rain=1 | WetGrass=1):",
      probability('Rain', 1, {'WetGrass': 1}))

print("P(Sprinkler=1 | WetGrass=1):",
      probability('Sprinkler', 1, {'WetGrass': 1}))

# -----------------------------
# Step 4: Joint Probability
# -----------------------------
def joint_probability(query, evidence):
    count = 0
    total = 0

    for row in data:
        if all(row[k] == v for k, v in evidence.items()):
            total += 1
            if all(row[k] == v for k, v in query.items()):
                count += 1

    return count / total if total != 0 else 0

print("\nP(Rain=1, Sprinkler=1 | WetGrass=1):",
      joint_probability({'Rain': 1, 'Sprinkler': 1}, {'WetGrass': 1}))