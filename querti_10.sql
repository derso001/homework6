SELECT subj.name AS course_name
FROM subjects subj
JOIN marks m ON subj.id = m.subject_id_fn
JOIN students s ON m.student_id_fn = s.id
JOIN lectors l ON subj.lector_id_fn = l.id
WHERE s.name = 'Ім’я студента' AND l.name = 'Ім’я викладача';