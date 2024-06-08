    SELECT 
    	AVG(mark) AS average_mark
    FROM marks m
    JOIN students s ON s.id = m.student_id
    JOIN subjects sub ON sub.id = m.subject_id 
    JOIN teachers t ON sub.teacher_id = t.id 
    WHERE s.id = 1 AND t.id = 3
    GROUP BY sub.name
;