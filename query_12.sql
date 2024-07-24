SELECT student, mark, lesson_datetime FROM
	(SELECT st.name AS student, m.value AS mark, m.created_at AS lesson_datetime,
	ROW_NUMBER () OVER (PARTITION BY st.name ORDER BY m.created_at desc) AS RN
	FROM students st
	LEFT JOIN subjects s
	ON m.student_id_fn  = st.id
	LEFT JOIN groups g
	ON st.group_id_fn  = g.id
	LEFT JOIN marks m
	ON m.subject_id_fn = s.id
	WHERE s.name  = 'Databases'
	AND g.name = 'IT')
WHERE RN = 1
