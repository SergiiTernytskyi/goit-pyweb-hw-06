    SELECT s.first_name, 
        s.last_name, 
        g.name AS group, 
        m.mark 
    FROM marks m
    JOIN students s ON m.student_id = s.id
    JOIN groups g ON g.id = s.group_id 
    JOIN subjects sub ON sub.id = m.subject_id
    WHERE g.id = %s AND sub.id = %s
;