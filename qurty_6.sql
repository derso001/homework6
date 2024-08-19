SELECT s.id, s.name
FROM students s
JOIN groups g ON s.groups_id_fn = g.id
WHERE g.name = 'Назва групи';