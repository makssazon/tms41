from school.models import session, Group, Student

result = session.query(Group, Student).\
    join(Student, Group.id == Student.group_id). \
    filter(Student.firstname == 'max')
for group, st in result:
    print(group.name, st.firstname)
