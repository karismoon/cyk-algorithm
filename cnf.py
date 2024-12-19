from library import example_cfg, example_cfg_with_epsilon
from cnf_helpers import eliminate_epsilon, eliminate_unit_productions, remove_mixed_productions, enforce_binary_productions

"""
example_cfg = {
    "a": ["A", "C"],
    "b": ["B"],
    "AB": ["S", "C"],
    "BC": ["S"],
    "BA": ["A"],
    "CC": ["B"],
}
"""

def convert_to_cnf(cfg):
    # Step 1: Augment grammar
    new_start_symbol = "S0"
    cfg[new_start_symbol] = ["S"]
    
    # Step 2: Eliminate epsilon-productions
    cfg = eliminate_epsilon(cfg)
    
    # Step 3: Eliminate unit productions
    cfg = eliminate_unit_productions(cfg)
    
    # Step 4: Remove mixed productions
    cfg = remove_mixed_productions(cfg)
    
    # Step 5: Enforce binary productions
    cfg = enforce_binary_productions(cfg)
    
    return cfg

print(example_cfg_with_epsilon)

converted = convert_to_cnf(example_cfg_with_epsilon)
print(converted)