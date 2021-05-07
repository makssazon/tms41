from school.models import session, Group, Student, Diary

result = session.query(Group, Student). \
    join(Student, Group.id == Student.group_id). \
    filter(Student.firstname == 'max')
for group, st in result:
    print(group.name, st.firstname)

print('-' * 15)

result2 = session.query(Student, Diary). \
    join(Diary, Student.id == Diary.student_id). \
    filter(Diary.avg_score > 6)
for st, d in result2:
    print(st.firstname, d.avg_score)
