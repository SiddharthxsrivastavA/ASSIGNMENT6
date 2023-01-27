def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")

    if 'student_class' in kwargs:
        print(f"Student Class: {kwargs['student_class']}")


student_data(student_id='22104095', student_name='Siddharth Srivastava')

student_data(student_id='22104095', student_name='Siddharth Srivastava', student_class='G2')
