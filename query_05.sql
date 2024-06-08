    SELECT t.first_name, 
        t.last_name, 
        s.name AS subject_name 
    FROM subjects s
    JOIN teachers t ON s.teacher_id = t.id
    WHERE t.id = 2;