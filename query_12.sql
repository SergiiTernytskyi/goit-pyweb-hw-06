    SELECT s.first_name, s.last_name,
    	m.mark, m.mark_date 
    FROM marks m
    JOIN students s ON s.id = m.student_id
    JOIN subjects sub ON sub.id = m.subject_id 
    JOIN groups g ON s.group_id = g.id 
    WHERE g.id = 1 AND sub.id = 2 AND m.mark_date = (
        SELECT
            MAX(mark_date) 
        FROM marks 
        WHERE subject_id = sub.id );