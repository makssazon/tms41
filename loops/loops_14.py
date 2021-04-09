# Создать список учеников подобной структуры. Определить
# средний балл каждого студента по всем предметам, и
# вывести сведения о студентах, средний балл которых больше
# 4. [02-7.3-BL-02]
# pupils = [
#   {
#         'firstname': 'Masha',
#         'Group': 42,
#         'physics': 7,
#         'informatics': 6,
#         'history': 8,
#   },
# ]
pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Sasha',
        'Group': 42,
        'physics': 3,
        'informatics': 4,
        'history': 5,
    },
    {
        'firstname': 'Dasha',
        'Group': 42,
        'physics': 10,
        'informatics': 3,
        'history': 8,
    },
    {
        'firstname': 'Igar',
        'Group': 42,
        'physics': 4,
        'informatics': 3,
        'history': 3,
    },

]

result = []
for pupil in pupils:
    total = 0
    for i, values in enumerate(pupil.values()):
        if i > 1:
            total += values
    avg = total / 3
    print(f'avg of {pupil["firstname"]} is {avg}')
    if avg > 4:
        result.append(pupil["firstname"])
print(f'names best pupils with avg > 4  - {", ".join(result)}')
