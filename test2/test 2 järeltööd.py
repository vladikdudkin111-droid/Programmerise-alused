"""VARIANT 4 (LÜHIKE): ÕPILASTE TULEMUSTE ANALÜÜS

ÜLESANDE KIRJELDUS:
Kool vajab lihtsat programmi õpilaste hinnete analüüsimiseks.

SISENDANDMED:
Fail "õpilased.txt" sisaldab õpilaste andmeid formaaadis:
Nimi;Klass

Näiteks:
Mati Maasikas;10A
Kati Kask;10B
Peeter Puu;10A

Fail "hinded.txt" sisaldab hindeid formaaadis:
Nimi;Aine;Hinne

Näiteks:
Mati Maasikas;Matemaatika;4
Mati Maasikas;Eesti keel;5
Kati Kask;Matemaatika;5

ÜLESANDED:

1. Loe mõlemad failid sisse ja salvesta andmed.

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik õpilased
   2 - Õpilase hinded
   3 - Klassi statistika
   4 - Salvesta kokkuvõte
   0 - Välju

3. KUVA KÕIK ÕPILASED: Prindi välja kõik õpilased koos klassiga.

4. ÕPILASE HINDED: Kasutaja sisestab õpilase nime.
   - Kuva õpilase klass
   - Kuva kõik tema hinded
   - Arvuta keskmine hinne
   - Määra, kas õpilane läbis (kõik hinded >= 3)

5. KLASSI STATISTIKA: Kasutaja sisestab klassi (nt "10A").
   - Kuva klassis olevad õpilased
   - Arvuta klassi keskmine hinne
   - Leia klassi parim õpilane (kõrgeim keskmine)

6. SALVESTA KOKKUVÕTE: Loo fail "tulemused_kokkuvõte.txt", kuhu kirjuta:
   - Õpilaste arv
   - Hinnete arv
   - Üldine keskmine hinne
   - Parim õpilane (kõrgeim keskmine)

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"
"""

def read_students(filename):
    students = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(";")
            if len(parts) != 2:
                print("Vigane rida:", line)
                continue

            name, class_name = parts
            students[name] = class_name

    return students


def read_grades(filename):
    grades = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue

            parts = line.split(";")

            if len(parts) != 3:
                print("Vigane rida:", line)
                continue

            name, subject, grade = parts
            grade = int(grade)

            if name not in grades:
                grades[name] = []

            grades[name].append((subject, grade))

    return grades


def show_all_students(students):
    print("\nKõik õpilased:")
    for name, class_name in students.items():
        print(f"{name} - {class_name}")


def student_grades(students, grades):
    name = input("Sisesta õpilase nimi: ")

    if name not in students:
        print("Õpilast ei leitud!")
        return

    print(f"Klass: {students[name]}")

    if name not in grades:
        print("Hinded puuduvad!")
        return

    grade_list = grades[name]

    total = 0
    passed = True

    for subject, grade in grade_list:
        print(f"{subject}: {grade}")
        total += grade
        if grade < 3:
            passed = False

    average = total / len(grade_list)
    print(f"Keskmine hinne: {average:.2f}")

    if passed:
        print("Staatus: Läbis")
    else:
        print("Staatus: Ei läbinud")


def class_statistics(students, grades):
    class_name = input("Sisesta klass (nt 10A): ")

    class_students = [name for name, c in students.items() if c == class_name]

    if not class_students:
        print("Klassi ei leitud!")
        return

    print("\nÕpilased klassis:")
    for name in class_students:
        print(name)

    total_sum = 0
    grade_count = 0

    best_student = None
    best_average = 0

    for name in class_students:
        if name in grades:
            grade_list = grades[name]
            s = sum(g for _, g in grade_list)
            avg = s / len(grade_list)

            total_sum += s
            grade_count += len(grade_list)

            if avg > best_average:
                best_average = avg
                best_student = name

    if grade_count > 0:
        class_avg = total_sum / grade_count
        print(f"Klassi keskmine hinne: {class_avg:.2f}")

    if best_student:
        print(f"Parim õpilane: {best_student} ({best_average:.2f})")


def save_summary(students, grades):
    student_count = len(students)

    grade_count = 0
    total_sum = 0

    best_student = None
    best_average = 0

    for name, grade_list in grades.items():
        grade_count += len(grade_list)
        s = sum(g for _, g in grade_list)
        total_sum += s

        avg = s / len(grade_list)

        if avg > best_average:
            best_average = avg
            best_student = name

    overall_avg = total_sum / grade_count if grade_count > 0 else 0

    with open("tulemused_kokkuvõte.txt", "w", encoding="utf-8") as f:
        f.write(f"Õpilaste arv: {student_count}\n")
        f.write(f"Hinnete arv: {grade_count}\n")
        f.write(f"Üldine keskmine hinne: {overall_avg:.2f}\n")
        if best_student:
            f.write(f"Parim õpilane: {best_student} ({best_average:.2f})\n")

    print("Kokkuvõte salvestatud faili tulemused_kokkuvõte.txt")


def menu():
    print("\n--- MENÜÜ ---")
    print("1 - Kuva kõik õpilased")
    print("2 - Õpilase hinded")
    print("3 - Klassi statistika")
    print("4 - Salvesta kokkuvõte")
    print("0 - Välju")


if __name__ == '__main__':
    students = read_students("õpilased.txt")
    grades = read_grades("hinded.txt")

    while True:
        menu()
        choice = input("Vali: ")

        if choice == "1":
            show_all_students(students)
        elif choice == "2":
            student_grades(students, grades)
        elif choice == "3":
            class_statistics(students, grades)
        elif choice == "4":
            save_summary(students, grades)
        elif choice == "0":
            print("Programm lõpetab töö.")
            break
        else:
            print("Vale valik!")