def correlation_ratio(data, category, values):
    categories = set(data[category])

    in_group = 0
    inter_group = 0
    avg = sum(data[values]) / len(data[values])
    for c in categories:
        c_data = data[data[category] == c][values]
        c_avg = sum(c_data) / len(c_data)
        c_group = 0
        inter_group += len(c_data) * (c_avg - avg) ** 2
        for v in c_data:
            c_group += (v - c_avg) ** 2
        in_group += c_group

    return round(inter_group / (in_group - inter_group), 4)
