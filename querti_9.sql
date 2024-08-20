SELECT subj.name AS course_name
FROM subjects subj
JOIN marks m ON subj.id = m.subject_id_fn
JOIN students s ON m.student_id_fn = s.id
WHERE s.name = 'Ім’я студента';