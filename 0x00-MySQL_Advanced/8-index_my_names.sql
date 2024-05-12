-- creating an index with the first word

CREATE index idx_name_first ON names(LEFT(names, 1));
