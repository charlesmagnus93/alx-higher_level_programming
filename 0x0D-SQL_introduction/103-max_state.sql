-- max temperature by state
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state ASC;
