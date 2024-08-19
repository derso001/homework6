SELECT subj.name AS course_name
FROM subjects subj
JOIN lectors l ON subj.lector_id_fn = l.id
WHERE l.name = "Ім'я викладача";