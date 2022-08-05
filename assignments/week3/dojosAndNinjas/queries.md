insert into dojos (name)
values ("Twitch"), ("Discord"), ("Zoom");

DELETE FROM dojos where id between 2 and 4;

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Caitlin","Grady",39,4),("jay","omeara",39,4),("angela","frank",30,4);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("kym","pitlor",33,5),("bobby","omeara",4,5),("sonny","omeara",1,5);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Shosh","dog",9,6),("Betty","Dog",2,6),("herman","cat",5,6);

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 4;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
	WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);
    
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);