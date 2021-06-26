#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output


def valid_name(name: str) -> bool:
    for letter in name:
        if not (letter.isalpha() or letter == " "):
            return False
    return True


def calc_final_grade(student_info: dict) -> int:
    id_number = 10 * int(student_info["id"][-2]) + int(student_info["id"][-1])
    return int((int(student_info["homework_avg"]) + id_number) / 2)


def find_min_student(output_students_dict: dict) -> (str, dict):
    min_student = ""
    for student, student_dict in output_students_dict.items():

        if min_student == "":
            min_student = student
            continue
        elif min_student > student:  # cannot be equal since the id is unique
            min_student = student

    return min_student, output_students_dict[min_student]


def final_grade(input_path: str, output_path: str) -> int:
    f = open(input_path, 'r')
    output_students_dict = {}

    for line in f:
        info_string = line.split(',')
        student_info_dict = {
            "id": info_string[0].strip(),
            "name": info_string[1].strip(),
            "semester": info_string[2].strip(),
            "homework_avg": info_string[3].strip()
        }
        if student_info_dict["id"][0] == "0" or len(student_info_dict["id"]) != 8:
            continue
        elif not valid_name(student_info_dict["name"]):
            continue
        elif int(student_info_dict["semester"]) < 1:
            continue
        elif int(student_info_dict["homework_avg"]) <= 50 or int(student_info_dict["homework_avg"]) > 100:
            continue

        else:
            output_students_dict[student_info_dict["id"]] = student_info_dict

    f.close()
    output_file = open(output_path, 'w')
    students_sum = 0
    students_amount = len(output_students_dict)

    while output_students_dict:
        student, student_info = find_min_student(output_students_dict)
        student_final_grade = calc_final_grade(output_students_dict[student])
        students_sum += student_final_grade
        output_file.write(f'{student}, {student_info["homework_avg"]}, {student_final_grade}\n')
        output_students_dict.pop(student)

    output_file.close()
    if students_amount != 0:
        return int(students_sum / students_amount)
    else:
        return 0


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:

    lowercase_s1 = s1.lower()
    lowercase_s2 = s2.lower()
    for letter_index in range(97, 123):  # looping through lowercase alphabet in ascii
        if lowercase_s1.count(chr(letter_index)) > lowercase_s2.count(chr(letter_index)):
            return False

    return True
