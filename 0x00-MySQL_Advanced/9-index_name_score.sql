--An index for first letter of name and scpre

CREATE INDEX idx_name_first_score ON names(LEFT(name, 1), score);
