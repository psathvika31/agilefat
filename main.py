def calculate_metrics(marks_list):
    if not marks_list:
        return {"total": 0, "average": 0}
    
    total = sum(marks_list)
    average = total / len(marks_list)
    return {"total": total, "average": round(average, 2)}

if __name__ == "__main__":
    # Test sample simulation run
    sample_marks = [85, 90, 78, 92]
    results = calculate_metrics(sample_marks)
    print(f"--- Student Grade Calculator (V1) ---")
    print(f"Marks Input: {sample_marks}")
    print(f"Total Marks: {results['total']}")
    print(f"Average Mark: {results['average']}")
