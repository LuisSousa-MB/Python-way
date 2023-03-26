def is_criticality_balanced(temperature, neutrons_emitted):
    is_over_heat = temperature > 800
    is_over_emitted = neutrons_emitted > 500
    return not is_over_heat and is_over_emitted

print(is_criticality_balanced(800,500))