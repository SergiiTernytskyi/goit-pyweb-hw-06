    SELECT g.name as group,    
        AVG(m.mark) as average_mark
    FROM marks m
    JOIN students s ON s.id = m.student_id
    JOIN groups g ON s.group_id = g.id
    JOIN subjects as sub ON m.subject_id = sub.id
    WHERE sub.id = %s 
    GROUP BY g.name
    ORDER BY g.name;