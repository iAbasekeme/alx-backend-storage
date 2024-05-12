-- A function that divides and returns the first by the second number or returns 0

DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE result INT; -- Define variable to hold result

    IF b = 0 THEN -- Check for division by zero
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END $$
DELIMITER ;
