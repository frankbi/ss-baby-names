LOAD DATA LOCAL INFILE 'babynames.csv'
INTO TABLE babynames
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(
	year,
	rank,
	name,
	gender,
	numM,
	numF
);