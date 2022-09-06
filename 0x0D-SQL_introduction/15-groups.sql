-- list number of score with the same score
SELECT score, number FROM second_table GROUP BY score as number ORDER BY score DESC;
