SELECT l.name AS lector, ROUND(AVG(m.value),1) AS AVG_score
FROM lectors l
LEFT JOIN subjects s
ON s.lector_id_fn  = l.id
LEFT JOIN marks m
ON m.subject_id_fn = s.id
WHERE l.name = 'Michael Hill'
GROUP BY 1
ORDER BY 1