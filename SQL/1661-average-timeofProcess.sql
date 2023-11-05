-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | machine_id     | int     |
-- | process_id     | int     |
-- | activity_type  | enum    |
-- | timestamp      | float   |
-- +----------------+---------+
-- The table shows the user activities for a factory website.
-- (machine_id, process_id, activity_type) is the primary key of this table.
-- machine_id is the ID of a machine.
-- process_id is the ID of a process running on the machine with ID machine_id.
-- activity_type is an ENUM of type ('start', 'end').
-- timestamp is a float representing the current time in seconds.
-- 'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
-- The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.


-- There is a factory website that has several machines each running the same number of processes. Write an SQL query to find the average time each machine takes to complete a process.

-- The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

-- The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

-- Return the result table in any order.

-- The query result format is in the following example.


-- Explicación de la consulta 

-- La consulta comienza seleccionando dos columnas: machine_id y ROUND(AVG(timestamp_end - timestamp_start), 3) como processing_time. La función ROUND se utiliza para redondear el resultado a 3 decimales.

-- Luego, se realiza una subconsulta para obtener los valores mínimos y máximos de timestamp para cada par (machine_id, process_id). Estos valores representan los tiempos de inicio y fin de cada proceso en una máquina.

-- A continuación, la consulta principal agrupa los resultados de la subconsulta por machine_id y calcula el promedio del tiempo de procesamiento (timestamp_end - timestamp_start) para cada máquina.

-- Finalmente, se obtiene una tabla con dos columnas: machine_id y processing_time, que muestra el machine_id y el tiempo promedio de procesamiento redondeado a 3 decimales para cada máquina.

-- Espero que esta explicación sea clara. Si tienes alguna otra pregunta, ¡no dudes en hacerla!


SELECT 
    machine_id,
    ROUND(AVG(timestamp_end - timestamp_start), 3) AS processing_time
FROM
    (SELECT
        machine_id,
        process_id,
        MIN(timestamp) AS timestamp_start,
        MAX(timestamp) AS timestamp_end
    FROM
        Activity
    GROUP BY
        machine_id,
        process_id) AS subquery
GROUP BY
    machine_id;


-- Input: 
-- Activity table:
-- +------------+------------+---------------+-----------+
-- | machine_id | process_id | activity_type | timestamp |
-- +------------+------------+---------------+-----------+
-- | 0          | 0          | start         | 0.712     |
-- | 0          | 0          | end           | 1.520     |
-- | 0          | 1          | start         | 3.140     |
-- | 0          | 1          | end           | 4.120     |
-- | 1          | 0          | start         | 0.550     |
-- | 1          | 0          | end           | 1.550     |
-- | 1          | 1          | start         | 0.430     |
-- | 1          | 1          | end           | 1.420     |
-- | 2          | 0          | start         | 4.100     |
-- | 2          | 0          | end           | 4.512     |
-- | 2          | 1          | start         | 2.500     |
-- | 2          | 1          | end           | 5.000     |
-- +------------+------------+---------------+-----------+
-- Output: 
-- +------------+-----------------+
-- | machine_id | processing_time |
-- +------------+-----------------+
-- | 0          | 0.894           |
-- | 1          | 0.995           |
-- | 2          | 1.456           |
-- +------------+-----------------+
-- Explanation: 
-- There are 3 machines running 2 processes each.
-- Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
-- Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
-- Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456



