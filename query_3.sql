SELECT g.name AS group_name, ROUND(AVG(m.value),1) AS AVG_score
FROM students st
LEFT JOIN marks m
ON st.id = m.student_id_fn
LEFT JOIN groups g
ON st.group_id_fn  = g.id
GROUP BY 1
ORDER BY 2 DESC