-- list number of score with the same score
SELECT score, COUNT(id) as number FROM second_table GROUP BY score ORDER BY number DESC;
