SELECT st.name AS student_name, ROUND(AVG(m.value),1) AS AVG_score
FROM students st
LEFT JOIN marks m
ON st.id = m.student_id_fn
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5