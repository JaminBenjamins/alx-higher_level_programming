-- A script that creates a unique ID of a table attribute
-- It does not fail if the table exists
CREATE TABLE IF NOT EXISTS unique_id (`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
