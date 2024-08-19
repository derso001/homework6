SELECT s.id, s.name, AVG(m.value) AS average_grade
FROM students s
JOIN marks m ON s.id = m.student_id_fn
JOIN subjects subj ON m.subject_id_fn = subj.id
WHERE subj.name = 'Назва предмета'
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 1;