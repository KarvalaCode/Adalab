### Evaluación Final Sara

## Ejercicios
USE sakila;

-- 1. Selecciona todos los nombres de las películas sin que aparezcan duplicados.
SELECT DISTINCT title
	FROM film;

-- 2. Muestra los nombres de todas las películas que tengan una clasificación de "PG-13".
SELECT title, 
       rating
	FROM film
	WHERE rating = 'PG-13';

-- 3. Encuentra el título y la descripción de todas las películas que contengan la palabra "amazing" en su descripción.
SELECT title, 
       description
	FROM film
	WHERE description LIKE '%amazing%';

-- 4. Encuentra el título de todas las películas que tengan una duración mayor a 120 minutos.
SELECT title, 
	   length
	FROM film
	WHERE length > 120;

-- 5. Recupera los nombres de todos los actores.
SELECT first_name
	FROM actor;

-- 6. Encuentra el nombre y apellido de los actores que tengan "Gibson" en su apellido.
SELECT first_name,
	   last_name
	FROM actor
    WHERE last_name LIKE '%Gibson%';
    
-- 7. Encuentra los nombres de los actores que tengan un actor_id entre 10 y 20.
SELECT actor_id, 
	   first_name
	FROM actor
    WHERE actor_id BETWEEN 10 AND 20;

-- 8. Encuentra el título de las películas en la tabla film que no sean ni "R" ni "PG-13" en cuanto a su clasificación.
SELECT title,
	   rating
	FROM film
	WHERE rating NOT IN ('R','PG-13');

-- 9. Encuentra la cantidad total de películas en cada clasificación de la tabla film y muestra la clasificación junto con el recuento.
SELECT rating,
	   COUNT(film_id) AS cantidad_peliculas
	FROM film
	GROUP BY rating;

-- 10. Encuentra la cantidad total de películas alquiladas por cada cliente y muestra el ID del cliente, su nombre y apellido junto con la cantidad de películas alquiladas.

	-- Join alquileres e inventario para tener asociados alquileres y películas (en rental no hay film_id esta en el inventario) 
    -- = LEFT que INNER porque todos los alquileres tienen una pelicula y un cliente asociado
    
WITH pelis_id_cliente AS (SELECT customer_id,
						         COUNT(film_id) AS peliculas_alquiladas
							  FROM rental 
							  LEFT JOIN inventory
							  ON rental.inventory_id = inventory.inventory_id
							  GROUP BY customer_id)
                          
	-- join con clientes para acceder a sus nombres y apellidos
    SELECT pelis_id_cliente.customer_id, 
           first_name, 
           last_name, 
           peliculas_alquiladas
		FROM pelis_id_cliente 
		LEFT JOIN customer
		ON  pelis_id_cliente.customer_id = customer.customer_id;
    
# OTRA OPCIÓN (joins seguidos)    
SELECT customer.customer_id, 
	   first_name, 
	   last_name, 
       COUNT(film_id) AS peliculas_alquiladas
	FROM rental 
    LEFT JOIN inventory
	ON rental.inventory_id = inventory.inventory_id
	-- join con clientes para acceder a sus nombres y apellidos
    LEFT JOIN customer
    ON  rental.customer_id = customer.customer_id
    GROUP BY customer_id;
    
-- contando rental_id en vez de film_id    
    SELECT customer.customer_id,
		   first_name, 
	       last_name,
           COUNT(rental_id) AS numero_peliculas_alquiladas
		FROM rental
        LEFT JOIN customer
		ON  rental.customer_id = customer.customer_id
        GROUP BY customer_id;
        
 -- comparando el numero de alquileres con el numero de pelieculas alquiladas (es lo mismo)        
	  SELECT customer.customer_id,
	         first_name, 
			 last_name,
	         COUNT(rental_id) AS numero_peliculas_rentals,
	         COUNT(film_id) AS peliculas_alquiladas_film
			FROM rental
			LEFT JOIN customer
			ON  rental.customer_id = customer.customer_id
			LEFT JOIN inventory
			ON rental.inventory_id = inventory.inventory_id
			GROUP BY customer_id;
    
-- 11. Encuentra la cantidad total de películas alquiladas por categoría y muestra el nombre de la categoría junto con el recuento de alquileres. (= LEFT que INNER porque hay alquileres de todas las categorias y todas las categorias tienen id y nombre)
							 
WITH alquiler_peli_categoria AS (SELECT rental_id,
									     alquiler_id_pelicula.film_id, 
                                         category_id
									FROM ( -- Join alquileres e inventario para tener asociados los id de alquileres y pelicula  
										   SELECT rental_id, 
												  film_id
											   FROM rental 
											   LEFT JOIN inventory
											   ON rental.inventory_id = inventory.inventory_id
										   ) AS alquiler_id_pelicula
									  -- join con pelicula - categorias para asociar la categoria a la pelicula       
									  LEFT JOIN film_category
									  ON alquiler_id_pelicula.film_id = film_category.film_id
                                  )
    
		-- join con categorias para asociar la categoria a la pelicula y contarlas
SELECT alquiler_peli_categoria.category_id, 
	   name, 
       COUNT(film_id) AS peliculas_alquiladas
	FROM alquiler_peli_categoria 
    LEFT JOIN category
	ON  alquiler_peli_categoria.category_id = category.category_id
    GROUP BY category_id; 
    
    # OTRA OPCIÓN (joins seguidos)    
SELECT film_category.category_id,
       name,
       COUNT(inventory.film_id) AS peliculas_alquiladas
	FROM rental 
    LEFT JOIN inventory
    ON rental.inventory_id = inventory.inventory_id
    LEFT JOIN film_category
	ON inventory.film_id = film_category.film_id
	LEFT JOIN category
	ON  film_category.category_id = category.category_id
    GROUP BY film_category.category_id;
    
    -- contando rental_id en vez de film_id (da lo mismo)
	SELECT film_category.category_id,
       name,
       COUNT(rental.rental_id) AS peliculas_alquiladas
		FROM rental 
		LEFT JOIN inventory
		ON rental.inventory_id = inventory.inventory_id
		LEFT JOIN film_category
		ON inventory.film_id = film_category.film_id
		LEFT JOIN category
		ON  film_category.category_id = category.category_id
		GROUP BY film_category.category_id;

-- 12. Encuentra el promedio de duración de las películas para cada clasificación de la tabla film y muestra la clasificación junto con el promedio de duración.
SELECT rating AS clasificacion, 
	   ROUND(AVG(length),2) AS promedio_duracion
	FROM film 
    GROUP BY rating; 

-- 13. Encuentra el nombre y apellido de los actores que aparecen en la película con title "Indian Love".
						-- join pelis y pelis-actor para asociar peli a id_actor, filtrar por el título concreto (= LEFT que INNER) y coseguir todos los id actores de esa pelicula
WITH pelis_id_actor AS (SELECT title,
							   actor_id
							FROM film_actor 
							LEFT JOIN film
							ON film_actor.film_id = film.film_id
							WHERE title = 'Indian Love')
    
    -- join con actores para obtener nombre y apellidos (= LEFT que INNER)
    SELECT first_name, 
           last_name,
           title
		FROM pelis_id_actor
        LEFT JOIN actor
        ON pelis_id_actor.actor_id = actor.actor_id;  
        
    # OTRA OPCIÓN (joins seguidos)    
SELECT first_name, 
		last_name,
        title   
	FROM film_actor 
	LEFT JOIN film
	ON film_actor.film_id = film.film_id
	LEFT JOIN actor
	ON film_actor.actor_id = actor.actor_id
	WHERE title = 'Indian Love'; 

-- 14. Muestra el título de todas las películas que contengan la palabra "dog" o "cat" en su descripción.

-- diferentes opciones segun la pòsicion en la palabra (da los mismo que '%dog%' o '%cat%').
SELECT title, 
	   description
	FROM film
	WHERE description LIKE '% dog %' 
       OR description LIKE '% cat %' 
       OR description LIKE 'cat %'
       OR description LIKE 'dog %'
	   OR description LIKE '% dog'
       OR description LIKE '% cat';
       
-- 15. Hay algún actor que no aparezca en ninguna película en la tabla film_actor: --> no hay ningún actor que no aparezca en alguna de las películas de la tabla film_actor (estan todos los id en las dos tablas(1-200))
SELECT actor_id 
	FROM actor 
    WHERE actor_id NOT IN (SELECT actor_id FROM film_actor);    

-- 16. Encuentra el título de todas las películas que fueron lanzadas entre el año 2005 y 2010.
SELECT title, 
	   release_year
	FROM film 
    WHERE release_year BETWEEN 2005 AND 2010;
    
-- 17. Encuentra el título de todas las películas que son de la misma categoría que "Family".
						-- join pelis y pelis - categoria para asociar la pelicula con el id de su categoria 
WITH pelis_categoria AS (SELECT title,
								film.film_id, 
								category_id
							 FROM film 
							 LEFT JOIN film_category
							 ON film.film_id = film_category.film_id)

	-- join con categoria para obtener el nombre de las catgorias y filtrar por 'Family'
SELECT title, 
	   name
	FROM pelis_categoria 
    LEFT JOIN category
	ON pelis_categoria.category_id = category.category_id
	WHERE name = 'Family';

	# OTRA OPCIÓN (joins seguidos)    
    SELECT title,
			name
		FROM film 
		LEFT JOIN film_category
		ON film.film_id = film_category.film_id
		LEFT JOIN category
		ON film_category.category_id = category.category_id
		WHERE name = 'Family';
    

-- 18. Muestra el nombre y apellido de los actores que aparecen en más de 10 películas. (todos los actores (14 - 42 peliculas por actor).
						 -- id actores en más de 10 peliculas
WITH actores_mas_d10 AS (SELECT actor_id, 
					            COUNT(film_id) AS numero_peliculas
							 FROM film_actor
							 GROUP BY actor_id
							 HAVING numero_peliculas > 10)

	-- join con actores para obtener nombre y apelliddos
SELECT first_name, 
	   last_name, 
       numero_peliculas
	FROM actores_mas_d10 
    LEFT JOIN actor
    ON actores_mas_d10.actor_id = actor.actor_id;

 	# OTRA OPCIÓN (joins seguidos)    
    SELECT first_name, 
	       last_name, 
		   COUNT(film_id) AS numero_peliculas
		 FROM film_actor
         LEFT JOIN actor
		 ON film_actor.actor_id = actor.actor_id
		 GROUP BY film_actor.actor_id
		 HAVING numero_peliculas > 10;

-- 19. Encuentra el título de todas las películas que son "R" y tienen una duración mayor a 2 horas en la tabla film (columna duracion en minutos --> 120 min).
SELECT title, 
	   rating, 
       length
	FROM film
	WHERE rating = 'R' 
	  AND length > 120;

-- 20. Encuentra las categorías de películas que tienen un promedio de duración superior a 120 minutos y muestra el nombre de la categoría junto con el promedio de duración.
							-- id categorias con promedio > 120 min
WITH categoria_mas_d120 AS (SELECT category_id, 
							       AVG(length) AS promedio_duracion
								FROM film 
								LEFT JOIN film_category
								ON film_category.film_id = film.film_id
								GROUP BY category_id
								HAVING promedio_duracion > 120)
                                
		-- join categoria para obtener el nombre de las categorias
SELECT  categoria_mas_d120.category_id,
		name, 
        promedio_duracion
	FROM categoria_mas_d120 
    LEFT JOIN category
    ON categoria_mas_d120.category_id = category.category_id;
    
     	# OTRA OPCIÓN (joins seguidos)    
		SELECT film_category.category_id, 
			   name,
			   AVG(length) AS promedio_duracion
			FROM film 
			LEFT JOIN film_category
			ON film_category.film_id = film.film_id
            LEFT JOIN category
			ON film_category.category_id = category.category_id
			GROUP BY category_id
			HAVING promedio_duracion > 120;
   
-- 21. Encuentra los actores que han actuado en al menos 5 películas y muestra el nombre del actor junto con la cantidad de películas en las que han actuado. (todos los actores (14 - 42 peliculas por actor).

						 -- id actores en mínimo 5 peliculas
WITH actores_mas_d10 AS (SELECT actor_id, 
						        COUNT(film_id) AS numero_peliculas
						 FROM film_actor
						 GROUP BY actor_id
                         HAVING numero_peliculas >= 5)

	-- join con actores para obtener nombre
SELECT first_name, 
	   numero_peliculas
	FROM actores_mas_d10 
    LEFT JOIN actor
    ON actores_mas_d10.actor_id = actor.actor_id;
    
	# OTRA OPCIÓN (joins seguidos)    
	SELECT actor.first_name, 
		   COUNT(film_id) AS numero_peliculas
		FROM film_actor
        LEFT JOIN actor
		ON film_actor.actor_id = actor.actor_id
		GROUP BY actor.actor_id
		HAVING numero_peliculas >= 5;
    
-- 22. Encuentra el título de todas las películas que fueron alquiladas por más de 5 días. Utiliza una subconsulta para encontrar los rental_ids (inventory_id) con una duración superior a 5 días y luego selecciona las películas correspondientes.

								     
WITH id_peli_alquiler_mas_d5 AS ( -- id alquiler y peli de alquileres de más de 5 días 
								  SELECT rental_id, film_id, duracion_alquiler
										-- subconsulta con id de alquiler e id de inventario para alquileres de mas de 5 dias
								 FROM (
										SELECT rental_id, 
										      inventory_id, 
											  DATEDIFF(return_date, rental_date) AS duracion_alquiler 
										   FROM rental
										   WHERE DATEDIFF(return_date, rental_date) > 5
                                       ) AS alquileres_mas_d5
										   LEFT JOIN inventory
										   ON alquileres_mas_d5.inventory_id = inventory.inventory_id
								)
-- join con peliculas para obtener el títitulo                                       
SELECT title, 
	   duracion_alquiler
	FROM id_peli_alquiler_mas_d5 
    LEFT JOIN film
    ON id_peli_alquiler_mas_d5.film_id = film.film_id;

	# OTRA OPCIÓN (joins seguidos) 
    SELECT title, 
		   DATEDIFF(return_date, rental_date) AS duracion_alquiler 
	   FROM rental
       LEFT JOIN inventory
	   ON rental.inventory_id = inventory.inventory_id
       LEFT JOIN film
       ON inventory.film_id = film.film_id
	   WHERE DATEDIFF(return_date, rental_date) > 5;

-- 23. Encuentra el nombre y apellido de los actores que no han actuado en ninguna película de la categoría "Horror". Utiliza una subconsulta para encontrar los actores que han actuado en películas de la categoría "Horror" y luego exclúyelos de la lista de actores.
-- actores no en la lista de actores  en pelis de horror
SELECT first_name, 
	   last_name
	FROM actor
	WHERE actor_id NOT IN   -- id actores en las pelis de categoria 'Horror'
						   (SELECT actor_id
							   FROM film_actor   
							   WHERE film_id IN   -- id pelis de categoria horror 
												 (SELECT film_id
													  FROM film_category
													  WHERE category_id =  -- id de la categoria 'Horror'
																		  (SELECT category_id
																			   FROM category
																			   WHERE name = 'Horror')));                       
-- 24. BONUS: Encuentra el título de las películas que son comedias y tienen una duración mayor a 180 minutos en la tabla film.
  
SELECT title
	FROM film
	WHERE length > 180
	  AND film_id IN   -- id pelis de categoria 'Comedy' 
					   (SELECT film_id
						   FROM film_category
						   WHERE category_id =  -- id de la categoria 'Comedy'
											   (SELECT category_id
													FROM category
													WHERE name = 'Comedy'));

-- 25. BONUS: Encuentra todos los actores que han actuado juntos en al menos una película. La consulta debe mostrar el nombre y apellido de los actores y el número de películas en las que han actuado juntos.
						-- query correlacionada para crear una tabla con los id de los actores que han coincidido en una pelicula junto al id de la pelicula
WITH pareja_actores AS (SELECT fa1.film_id,
							   fa1.actor_id AS id_interprete1, 
                               fa2.actor_id AS id_interprete2
							FROM film_actor AS fa1 
							INNER JOIN (SELECT actor_id,
											   film_id
										FROM film_actor) AS fa2
							ON fa1.film_id = fa2.film_id
							WHERE fa1.actor_id != fa2.actor_id)
    
SELECT id_interprete1,
	   id_interprete2,
       CONCAT(a1.first_name, ' ', a1.last_name) AS nombre_interprete1,
       CONCAT(a2.first_name, ' ',  a2.last_name) AS nombre_interprete2,
       COUNT(DISTINCT film_id) AS numero_peliculas
	FROM pareja_actores LEFT JOIN actor AS a1
    ON pareja_actores.id_interprete1 = a1.actor_id
    LEFT JOIN actor AS a2
    ON pareja_actores.id_interprete2 = a2.actor_id
    GROUP BY id_interprete1, id_interprete2;
    
# OTRA OPCIÓN (joins seguidos) 
SELECT fa1.actor_id AS id_interprete1, 
	   fa2.actor_id AS id_interprete2,
       CONCAT(a1.first_name, ' ', a1.last_name) AS nombre_interprete1,
       CONCAT(a2.first_name, ' ',  a2.last_name) AS nombre_interprete2,
       COUNT(DISTINCT fa1.film_id) AS numero_peliculas
	FROM film_actor AS fa1 
	INNER JOIN (SELECT actor_id,
					   film_id
				FROM film_actor) AS fa2
	ON fa1.film_id = fa2.film_id
	LEFT JOIN actor AS a1
    ON fa1.actor_id = a1.actor_id
    LEFT JOIN actor AS a2
    ON fa2.actor_id = a2.actor_id
    GROUP BY fa1.actor_id, fa2.actor_id
	HAVING fa1.actor_id != fa2.actor_id;