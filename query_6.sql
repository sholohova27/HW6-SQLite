SELECT st.name AS student_name
FROM students st
LEFT JOIN groups g
ON st.group_id_fn = g.id
WHERE g.name = 'IT'
ORDER BY 1