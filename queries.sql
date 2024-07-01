-- SIMPLE
SELECT *
FROM routes
ORDER BY  route_length;

-- MODERATE
-- Group routes by their starting point, then order by most number of same starting point
SELECT start_route, COUNT(*) count
FROM routes
GROUP BY start_route
HAVING count > 1
ORDER BY count DESC;

-- DIFFICULT
-- Routes of a given operator name (input for name_of_operator)
SELECT o.operator_number, r.route_id, r.start_route, r.end_route
FROM operators o
JOIN vehicles v ON v.operator_number = o.operator_number
JOIN routes r ON r.route_id = v.route_id
WHERE o.name_of_operator = "Haruki Murakami";
