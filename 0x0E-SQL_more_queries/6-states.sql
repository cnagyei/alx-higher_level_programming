-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to new database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (id)
);
