SELECT g.name AS group_name, AVG(m.value) AS average_grade
FROM groups g
JOIN students s ON g.id = s.groups_id_fn
JOIN marks m ON s.id = m.student_id_fn
JOIN subjects subj ON m.subject_id_fn = subj.id
WHERE subj.name = 'Назва предмета'
GROUP BY g.name;