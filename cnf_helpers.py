def eliminate_epsilon(cfg):
    print("Identifying nullable variables")
    nullable = set()

    # Find nullable variables
    for head, productions in cfg.items():
        for production in productions:
            if production == "ε":
                nullable.add(head)

    print("Nullable variables:", nullable)

    # Remove epsilon-productions and update grammar
    new_cfg = {}
    for head, productions in cfg.items():
        new_cfg[head] = []
        for production in productions:
            if production != "ε":
                new_cfg[head].append(production)
                # Add productions by removing nullable symbols
                for nullable_symbol in nullable:
                    if nullable_symbol in production:
                        new_cfg[head].append(production.replace(nullable_symbol, ""))
    return new_cfg

def eliminate_unit_productions(cfg):
    # Replace unit productions recursively
    return cfg

def remove_mixed_productions(cfg):
    # Replace terminal + non-terminal productions with proper rules
    return cfg

def enforce_binary_productions(cfg):
    # Break large productions into binary ones
    return cfg