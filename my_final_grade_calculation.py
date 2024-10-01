def my_final_grade_calculation(filename):
    results = {}
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0].strip().lower()
            scores = list(map(int, [part.strip() for part in parts[1:]]))
            
            quizzes = scores[:6]
            assignments = scores[6:10]
            midterm = scores[10]
            final = scores[11]
            
            quizzes.sort()
            quizzes_average = sum(quizzes[2:]) / 4
            
            assignments.sort()
            assignments_average = sum(assignments[1:]) / 3
            
            total_score = (quizzes_average * 0.25) + (assignments_average * 0.25) + (midterm * 0.25) + (final * 0.25)
            
            if total_score >= 60:
                results[name] = "pass"
            else:
                results[name] = "fail"
    
    return results

