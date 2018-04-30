.read sp17data.sql
.read fa17data.sql

CREATE TABLE obedience AS
  SELECT seven, denero, hilfinger FROM STUDENTS;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 18 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  SELECT fa.date, fa.color, fa.pet, fa.number, sp.number FROM sp17students as sp, students as fa WHERE fa.date = sp.date AND fa.color = sp.color AND fa.pet = sp.pet;

CREATE TABLE sevens AS
  SELECT st.seven FROM students AS st, checkboxes AS ch WHERE st.number = 7 AND ch.'7'='True' AND st.time = ch.time;

CREATE TABLE matchmaker AS
  SELECT p1.pet, p1.song, p1.color, p2.color FROM students as p1, students as p2 WHERE p1.pet=p2.pet AND p1.song = p2.song AND p1.time <> p2.time AND p1.time < p2.time;
