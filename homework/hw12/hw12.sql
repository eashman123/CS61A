CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name, sizes.size FROM dogs, sizes WHERE dogs.height>sizes.min AND dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT parents.child FROM dogs, parents WHERE parents.parent = dogs.name ORDER BY height DESC;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT s1.name || " and " || s2.name || " are " || s1.size || " siblings" FROM size_of_dogs as s1, size_of_dogs as s2, parents as p1, parents as p2
  WHERE s1.size = s2.size AND p1.parent = p2.parent AND p1.child = s1.name AND p2.child = s2.name AND s1.name<s2.name AND s1.name != s2.name;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
	WITH stacked(names, tot, i, max) AS (
	SELECT name, height, 1, height FROM DOGS UNION
	SELECT names || ', ' || name, tot + height, i+1, height FROM stacked, dogs WHERE i <= 4 AND max < height)
  SELECT names, tot FROM stacked WHERE i = 4 AND tot >= 170 ORDER BY tot;
