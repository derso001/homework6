SELECT s.id, s.name, m.value, m.timestamp
FROM students s
JOIN marks m ON s.id = m.student_id_fn
JOIN subjects subj ON m.subject_id_fn = subj.id
JOIN groups g ON s.groups_id_fn = g.id
WHERE g.name = 'Назва групи' AND subj.name = 'Назва предмета';