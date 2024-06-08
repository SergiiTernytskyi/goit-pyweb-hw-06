    SELECT 
    	sub.name as subject_name
    FROM subjects sub
    JOIN marks m ON m.subject_id = sub.id 
    JOIN students s ON s.id = m.student_id
    JOIN teachers t ON sub.teacher_id = t.id 
    WHERE s.id = 2 AND t.id = 1
    GROUP BY sub.name;