SELECT AVG(m.value) AS average_grade
FROM marks m
JOIN subjects subj ON m.subject_id_fn = subj.id
JOIN lectors l ON subj.lector_id_fn = l.id
WHERE l.name = 'Ім'я викладача';