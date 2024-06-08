    SELECT s.id,
        s.first_name,
        s.last_name,
        AVG(m.mark) as average_mark
    FROM students s
    JOIN marks m ON s.id = m.student_id  
    GROUP BY s.id
    ORDER BY average_mark ASC
    LIMIT 5;