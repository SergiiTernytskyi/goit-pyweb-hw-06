    SELECT AVG(m.mark) as average_mark 
    FROM marks m
    JOIN subjects sub ON sub.id = m.subject_id 
    JOIN teachers t ON t.id = sub.teacher_id
    WHERE t.id = %s;