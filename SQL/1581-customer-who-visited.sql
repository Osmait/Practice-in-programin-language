-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | visit_id    | int     |
-- | customer_id | int     |
-- +-------------+---------+
-- visit_id is the primary key for this table.
-- This table contains information about the customers who visited the mall.


-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | transaction_id | int     |
-- | visit_id       | int     |
-- | amount         | int     |
-- +----------------+---------+
-- transaction_id is the primary key for this table.
-- This table contains information about the transactions made during the visit_id.


-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | transaction_id | int     |
-- | visit_id       | int     |
-- | amount         | int     |
-- +----------------+---------+
-- transaction_id is the primary key for this table.
-- This table contains information about the transactions made during the visit_id.



-- Explicación de la consulta:

-- Selecciona las columnas Customer_id y COUNT(*) (número de registros) como count_no_trans.

-- Especifica la tabla de la cual se obtendrán los datos, en este caso, "Visits".

-- La cláusula WHERE filtra los registros de la tabla "Visits". La condición utilizada es visit_id NOT IN (SELECT DISTINCT visit_id FROM Transactions), lo que significa que solo se seleccionarán las visitas que no tienen su visit_id presente en la subconsulta. La subconsulta (SELECT DISTINCT visit_id FROM Transactions) obtiene todos los visit_id únicos de la tabla "Transactions".

-- Se utiliza la cláusula GROUP BY para agrupar los resultados por customer_id, lo que significa que se contará el número de visitas para cada cliente.

-- En resumen, la consulta devuelve una tabla con dos columnas: Customer_id y count_no_trans, donde count_no_trans representa el número de visitas de cada cliente en la tabla "Visits" que no tienen transacciones asociadas en la tabla "Transactions".

-- Espero que esta explicación sea útil. Si tienes más preguntas, no dudes en hacerlas.

-- V1
SELECT Customer_id, COUNT(*) as count_no_trans
FROM Visits
WHERE visit_id NOT  IN (SELECT DISTINCT visit_id FROM  Transactions)
GROUP BY customer_id;


-- V2
SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM visits v
LEFT JOIN transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;





-- Input: 
-- Visits
-- +----------+-------------+
-- | visit_id | customer_id |
-- +----------+-------------+
-- | 1        | 23          |
-- | 2        | 9           |
-- | 4        | 30          |
-- | 5        | 54          |
-- | 6        | 96          |
-- | 7        | 54          |
-- | 8        | 54          |
-- +----------+-------------+
-- Transactions
-- +----------------+----------+--------+
-- | transaction_id | visit_id | amount |
-- +----------------+----------+--------+
-- | 2              | 5        | 310    |
-- | 3              | 5        | 300    |
-- | 9              | 5        | 200    |
-- | 12             | 1        | 910    |
-- | 13             | 2        | 970    |
-- +----------------+----------+--------+
-- Output: 
-- +-------------+----------------+
-- | customer_id | count_no_trans |
-- +-------------+----------------+
-- | 54          | 2              |
-- | 30          | 1              |
-- | 96          | 1              |
-- +-------------+----------------+
-- Explanation: 
-- Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
-- Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
-- Customer with id = 30 visited the mall once and did not make any transactions.
-- Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
-- Customer with id = 96 visited the mall once and did not make any transactions.
-- As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.