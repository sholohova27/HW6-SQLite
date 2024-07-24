select s.name AS subject_name
FROM subjects s
LEFT JOIN lectors l
ON s.lector_id_fn  = l.id
WHERE l.name = 'Michael Hill'
ORDER BY 1