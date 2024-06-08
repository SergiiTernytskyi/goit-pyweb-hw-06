    SELECT s.id,
        s.first_name,
        s.last_name,
        AVG(m.mark) as average_mark
    FROM marks m
    JOIN students s ON s.id = m.student_id
    WHERE m.subject_id = 1 
    GROUP BY s.id
    LIMIT 1;