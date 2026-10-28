from main import calculate_metrics

def test_calculate_metrics():
    marks = [80, 90, 70]
    metrics = calculate_metrics(marks)
    assert metrics["total"] == 240
    assert metrics["average"] == 80.0

def test_empty_marks():
    metrics = calculate_metrics([])
    assert metrics["total"] == 0
    assert metrics["average"] == 0
