SELECT st.name AS student_name, s.name AS subject, m.value AS mark
FROM students st
LEFT JOIN marks m
ON st.id = m.student_id_fn
LEFT JOIN subjects s
ON s.id = m.subject_id_fn
LEFT JOIN groups g
ON st.group_id_fn = g.id
WHERE g.name = 'IT'
AND s.name = 'Data Science'
GROUP BY 1
ORDER BY 1
