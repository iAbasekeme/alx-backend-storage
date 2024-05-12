--A script that creates a stored procedure

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
    BEGIN
        SELECT AVG(score) AS average_score
        FROM corrections 
        WHERE user_id
        INTO average_score
    END $$
DELIMITER ;
