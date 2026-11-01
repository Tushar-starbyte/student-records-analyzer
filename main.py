def main():

    subjects = ("Python", "Maths", "DBMS")
    student_records = {}
    student_ids = []

    count_input = input("How many students to enter? ")
    num_students = int(count_input)

    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        student_id = input("Enter Student ID: ")

        if student_id in student_records:
            print("ID already exists! Skipping...")
            continue

        name = input("Enter Name: ")
        marks_list = []

        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))
            marks_list.append(mark)

        student_records[student_id] = {
            "name": name,
            "marks": marks_list
        }
        student_ids.append(student_id)

    if len(student_records) == 0:
        print("\nNo records entered.")
        return

    print("\n========== STUDENT REPORT ==========")
    all_averages = []

    for s_id in student_records:
        s_name = student_records[s_id]["name"]
        marks = student_records[s_id]["marks"]

        total = sum(marks)
        avg = total / len(marks)
        all_averages.append(avg)

        if avg >= 75:
            result = "Distinction"
        elif avg >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print(f"ID: {s_id} | Name: {s_name}")
        print(f"{subjects[0]}: {marks[0]}, {subjects[1]}: {marks[1]}, {subjects[2]}: {marks[2]}")
        print(f"Total: {total} | Average: {avg:.2f} | Result: {result}")
        print("-" * 35)

    print("\n----- LIST INDEXING & SLICING -----")
    print("First recorded ID:", student_ids[0])
    if len(student_ids) >= 2:
        print("First two IDs (Slicing):", student_ids[0:2])
    print("-----------------------------------")

    print("\n----- SET ANALYSIS -----")
    unique_subjects = set(subjects)
    print("Unique Subjects (Set):", unique_subjects)
    print("------------------------")

    class_avg = sum(all_averages) / len(all_averages)
    print("\n========== CLASS SUMMARY ==========")
    print("Total Students:", len(student_records))
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Average: {max(all_averages):.2f}")
    print(f"Lowest Average: {min(all_averages):.2f}")
    print("===================================")

if __name__ == "__main__":
    main()
