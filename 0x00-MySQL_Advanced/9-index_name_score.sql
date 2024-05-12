--An index for first letter of name and scpre

CREATE INDEX idx_name_first_score ON names(name(1), score);
