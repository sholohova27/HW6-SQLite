import sqlite3
import logging
import faker
import random

import table
import students
import groups
import marks
import subjects
import lectors


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('line_num: %(lineno)s > %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

fake_data = faker.Faker()


def generate_fake_students(students_table, number, start_id, group_id):
    student_id = []

    for i in range(start_id, start_id + number):
        students_table.create(
            students.Student(i,
                             fake_data.name(),
                             fake_data.random_element(group_id)
                             )
        )
        student_id.append(i)
    return student_id


def generate_fake_groups(groups_table, number, start_id):
    group_id = []
    used_words = set()
    group_list = ['Marketing', 'IT', 'PR', 'Art', 'Literature', 'History']

    for i in range(start_id, start_id + number):
        while True:
            group = random.choice(group_list)
            if group not in used_words:
                break
        used_words.add(group)

        groups_table.create(
            groups.Group(i,
                         group
                         )
        )
        group_id.append(i)
    return group_id


def generate_fake_marks(marks_table, number, start_id, subject_id, student_id):
    for i in range(start_id, start_id + number):
        marks_table.create(
            marks.Mark(id=i,
                       value=fake_data.random_int(min=1, max=100),
                       subject_id_fn=fake_data.random_element(subject_id),
                       student_id_fn=fake_data.random_element(student_id)
                       )
        )


def generate_fake_lectors(lectors_table, number, start_id):
    lector_id = []

    for i in range(start_id, start_id + number):
        lectors_table.create(
            lectors.Lector(i, fake_data.name()
                           )
        )
        lector_id.append(i)
    return lector_id


def generate_fake_subjects(subjects_table, number, start_id, lector_id):
    subject_id = []
    subject_list = ['Math', 'Literature', 'History', 'Databases', 'Data Science']
    used_subjects = set()

    for i in range(start_id, start_id + number):
        while True:
            subject = random.choice(subject_list)
            if subject not in used_subjects:
                break
        used_subjects.add(subject)

        subjects_table.create(
            subjects.Subject(i,
                             subject,
                             lector_id_fn=fake_data.random_element(lector_id)
                             )
        )
        subject_id.append(i)
    return subject_id


def main():
    with sqlite3.connect("my_db.sqlite") as conn:
        table.Table.conn = conn

        logging.debug("Database connection established")

        students_table = students.Students()
        groups_table = groups.Groups()
        marks_table = marks.Marks()
        subjects_table = subjects.Subjects()
        lectors_table = lectors.Lectors()

        # group_id = generate_fake_groups(groups_table, 3, 1)
        # student_id = generate_fake_students(students_table, 30,1, group_id)
        # lector_id = generate_fake_lectors(lectors_table, 5, 1)
        # subject_id = generate_fake_subjects(subjects_table, 5, 1, lector_id)
        # generate_fake_marks(marks_table, 1500, 1, subject_id, student_id)

        query_file = 'query_3.sql'

        with open(query_file, 'r') as file:
            query = file.read()

        results = students_table.select(query)
        for result in results:
            print(result)


if __name__ == '__main__':
    main()
