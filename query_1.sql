SELECT s.id, s.name, AVG(m.value) AS average_grade
FROM students s
JOIN marks m ON s.id = m.student_id_fn
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 5;