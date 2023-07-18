-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) as temp FROM temperatures GROUP BY city ORDER BY temp DESC;
