/* 
 * Check if mock data for Operators and Vehicles match: an Operator's no_of_operational_units must equal number of vehicles in Vehicles
 * Also an Operator's occupation (e.g., Bus, PUJ, UV) must match their vehicle's type
 * To check: just scanned the tables if the needed columns match :')
 */

-- Join operators on vehicles, group by operator number, and check if no_operational_units equal to count per group
 SELECT o.operator_number, o.no_of_operational_units, COUNT(*)
 FROM vehicles v
 JOIN operators o ON v.operator_number = o. operator_number
 GROUP BY o.operator_number;

-- Check if operator occupation matches their vehicles' type
 SELECT o.operator_number, v.plate_number, v.vehicle_type, o.occupation
 FROM vehicles v
 JOIN operators o ON v.operator_number = o. operator_number
 ORDER BY o.operator_number;