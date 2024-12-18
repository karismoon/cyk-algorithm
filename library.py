# keys are transformation results
# this is the cfg from the example video
example_cfg = {
    "a": ["A", "C"],
    "b": ["B"],
    "AB": ["S", "C"],
    "BC": ["S"],
    "BA": ["A"],
    "CC": ["B"],
}

example_cfg_with_epsilon = {
    "S": ["AB", "AC", "ε"],
    "A": ["a", "ε"],
    "B": ["b", "C"],
    "C": ["c", "ε"]
}
