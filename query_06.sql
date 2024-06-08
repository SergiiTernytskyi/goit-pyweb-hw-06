    SELECT s.first_name, 
        s.last_name, 
    FROM students s
    JOIN groups g ON s.group_id = g.id
    WHERE g.id = %s;