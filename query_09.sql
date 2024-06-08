    SELECT 
        sub.name as subject_name
    FROM subjects sub
    JOIN marks m ON m.subject_id = sub.id 
    JOIN students s ON s.id = m.student_id
    WHERE s.id = 2
    GROUP BY sub.name;
  