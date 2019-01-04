BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `category` (
	`categoryid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`description`	TEXT,
	`image`	TEXT
);
INSERT INTO `category` VALUES (1,'Hiking','hiking.png');
INSERT INTO `category` VALUES (2,'Climbing','climbing.png');
CREATE TABLE IF NOT EXISTS `article` (
	`articleid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`description`	TEXT,
	`price`	REAL,
	`image`	TEXT,
	`categoryid`	INTEGER,
	FOREIGN KEY(`categoryid`) REFERENCES `category`(`categoryid`)
);
INSERT INTO `article` VALUES (1,'Hiking pants',20.0,'hiking_pants.png',1);
INSERT INTO `article` VALUES (2,'Boots',50.0,'hiking_boots.png',1);
INSERT INTO `article` VALUES (3,'Climbing shoes',50.0,'climbing_shoes.png',2);
INSERT INTO `article` VALUES (4,'Climbing pants',30.0,'climbing_pants.png',2);
INSERT INTO `article` VALUES (5,'Carabiner',40.0,'climbing_carabiner.png',2);
INSERT INTO `article` VALUES (6,'Long rope',100.0,'climbing_rope.png',2);
INSERT INTO `article` VALUES (7,'Quickdraw pack',65.0,'climbing_quickdraw.png',2);
COMMIT;
