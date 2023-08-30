import itertools

condition = [
    ["民族=汉族", '民族!=汉族'],
    ["身份证号前两位=65", "身份证号前两位!=65"],
    ["籍贯=新疆", "籍贯!=新疆"]
]


def case_func(conditions):
    combinations = list(itertools.product(*conditions))
    case = []
    for combination in combinations:
        conditions_list = list(itertools.combinations(combination, 3))[0]
        # print(conditions_list)
        # print(",".join(conditions_list))
        case.append(",".join(conditions_list))
    return case


print(case_func(condition))
