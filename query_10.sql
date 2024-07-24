SELECT s.name AS subject_name
FROM students st
LEFT JOIN marks m
ON st.id = m.student_id_fn
LEFT JOIN subjects s
ON s.id = m.subject_id_fn
LEFT JOIN lectors l
ON s.lector_id_fn  = l.id
WHERE st.name = 'Sharon Bradley'
AND l.name = 'Michael Hill'
GROUP BY 1
ORDER BY 1