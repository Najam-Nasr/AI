from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# making the network
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# probabilities (priors)
cpd_I = TabularCPD('Intelligence', 2, [[0.7], [0.3]])
cpd_S = TabularCPD('StudyHours', 2, [[0.6], [0.4]])
cpd_D = TabularCPD('Difficulty', 2, [[0.4], [0.6]])

# Grade CPT
cpd_G = TabularCPD(
    'Grade', 3,
    [
        [0.5, 0.7, 0.2, 0.4, 0.2, 0.3, 0.05, 0.1],
        [0.3, 0.2, 0.5, 0.4, 0.4, 0.4, 0.25, 0.3],
        [0.2, 0.1, 0.3, 0.2, 0.4, 0.3, 0.7, 0.6]
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)

# Pass CPT
cpd_P = TabularCPD(
    'Pass', 2,
    [
        [0.05, 0.20, 0.50],
        [0.95, 0.80, 0.50]
    ],
    evidence=['Grade'],
    evidence_card=[3]
)

# adding everything
model.add_cpds(cpd_I, cpd_S, cpd_D, cpd_G, cpd_P)

model.check_model()

# inference part
infer = VariableElimination(model)

# query 1
result1 = infer.query(
    variables=['Pass'],
    evidence={'StudyHours': 0, 'Difficulty': 0}
)

print("P(Pass | StudyHours=Sufficient, Difficulty=Hard)")
print("No:", round(result1.values[0], 3))
print("Yes:", round(result1.values[1], 3))

# query 2
result2 = infer.query(
    variables=['Intelligence'],
    evidence={'Pass': 1}
)

print("\nP(Intelligence | Pass=Yes)")
print("High:", round(result2.values[0], 3))
print("Low:", round(result2.values[1], 3))
