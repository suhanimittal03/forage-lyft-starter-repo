def add_years_to_date(origjinal_date, years_to_add):
    result = origjinal_date.replace(year=origjinal_date.year + years_to_add)
    return result