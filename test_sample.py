import numpy as np

print("Starting pytest")

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

def nump_test_answer():
    y = np.array([3,4])
    assert inc(y[0]) == y[1]
    
print("Testing complete")
