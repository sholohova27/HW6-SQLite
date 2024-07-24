SELECT ROUND(AVG(m.value),1) AS AVG_score
FROM lectors l
LEFT JOIN subjects s
ON s.lector_id_fn  = l.id
LEFT JOIN marks m
ON m.subject_id_fn = s.id
LEFT JOIN students st
ON m.student_id_fn  = st.id
WHERE l.name = 'Michael Hill'
AND st.name  = 'Teresa Chavez'