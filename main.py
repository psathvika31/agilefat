def calculate_metrics(marks_list):
    if not marks_list:
        return {"total": 0, "average": 0, "grade": "F"}
    
    total = sum(marks_list)
    average = total / len(marks_list)
    
    # New Phase 2 Integration Logic
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return {"total": total, "average": round(average, 2), "grade": grade}

if __name__ == "__main__":
    sample_marks = [85, 90, 78, 92]
    results = calculate_metrics(sample_marks)
    print(f"--- Student Grade Calculator (V2) ---")
    print(f"Marks Input: {sample_marks}")
    print(f"Total Marks: {results['total']}")
    print(f"Average Mark: {results['average']}")
    print(f"Assigned Grade: {results['grade']}")
