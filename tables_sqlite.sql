-- Assumes there is an existing database which we create the following tables in
CREATE TABLE operators (
    operator_number CHAR(8) PRIMARY KEY,
    name_of_operator VARCHAR(50) NOT NULL,
    address VARCHAR(30) NOT NULL,
    occupation CHAR(15) CHECK (occupation IN ('Bus Operator', 'PUJ Operator', 'UV Operator'))  NOT NULL,
    no_of_operational_units INTEGER NOT NULL,
    age INTEGER CHECK (age >= 0) NOT NULL,
    contact_number CHAR(10) NOT NULL
);

CREATE TABLE routes (
    route_id CHAR(8) PRIMARY KEY,
    start_route VARCHAR(40) NOT NULL,
    end_route VARCHAR(40) NOT NULL,
    route_length DECIMAL(3, 0) CHECK (route_length >= 0),
    base_fare INTEGER CHECK (base_fare >= 0) NOT NULL
);

CREATE TABLE components (
    model VARCHAR(10) PRIMARY KEY,
    brake_system DECIMAL(6, 2) CHECK (brake_system >= 0),
    clutch DECIMAL(6, 2) CHECK (clutch >= 0),
    tires DECIMAL(6, 2) CHECK (tires >= 0),
    battery DECIMAL(6, 2) CHECK (battery >= 0),
    bearings DECIMAL(6, 2) CHECK (bearings >= 0),
    belt DECIMAL(6, 2) CHECK (belt >= 0),
    fuel_filter DECIMAL(6, 2) CHECK (fuel_filter >= 0),
    piston_ring DECIMAL(6, 2) CHECK (piston_ring >= 0),
    lights DECIMAL(6, 2) CHECK (lights >= 0),
    body DECIMAL(6, 2) CHECK (body >= 0),
    electrical_system DECIMAL(6, 2) CHECK (electrical_system >= 0)
);

CREATE TABLE vehicles (
    plate_number CHAR(8) PRIMARY KEY,
    vehicle_type CHAR(3) CHECK (vehicle_type IN ('Bus', 'PUJ', 'UV')) NOT NULL,
    manufacturer VARCHAR(30) NOT NULL,
    model VARCHAR(30),
    year INTEGER CHECK (year BETWEEN 0 AND 2024) NOT NULL,
    revenue DECIMAL(6, 2) CHECK (revenue >= 0) NOT NULL,
    engine_condition CHAR CHECK (engine_condition IN ('Good', 'Bad')) NOT NULL,
    seat_capacity INTEGER CHECK (seat_capacity BETWEEN 0 AND 999),
    operation_times CHAR(12) NOT NULL,
    operator_number CHAR(8),
    route_id CHAR(8),
    FOREIGN KEY (model) REFERENCES components(model) ON DELETE SET NULL,
    FOREIGN KEY (operator_number) REFERENCES operators(operator_number) ON DELETE SET NULL,
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE SET NULL
);
