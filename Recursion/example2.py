
# question: Mam wants total no of rows in the class room

def get_row_count(benchno):
    if benchno == 5:
        return 1
    else:
        return 1 + get_row_count(benchno + 1)

print(get_row_count(1))

