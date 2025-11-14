USE `lab4`;

INSERT INTO panel_type (type_name, description) VALUES
('Monocrystalline', 'High efficiency and longevity'),
('Polycrystalline', 'Good efficiency, affordable'),
('Thin Film', 'Lightweight and flexible'),
('Bifacial', 'Double-sided energy production'),
('PERC', 'High performance in low light'),
('IBC', 'High efficiency, lower losses'),
('Hybrid', 'Efficient under different conditions'),
('Organic', 'Eco-friendly materials'),
('Flexible', 'Ideal for portable devices'),
('CdTe', 'Thin film technology'),
('CIGS', 'Thin film, robust performance'),
('DSSC', 'Transparent and colorful'),
('Amorphous Silicon', 'Cost-effective thin film'),
('Multijunction', 'Very high efficiency'),
('Concentrated PV', 'High efficiency with lenses');

INSERT INTO location (city, street) VALUES
('Kyiv', 'Shevchenka St.'),
('Lviv', 'Halytska St.'),
('Odessa', 'Deribasivska St.'),
('Dnipro', 'Yavornytskoho Ave.'),
('Kharkiv', 'Sumska St.'),
('Cherkasy', 'Khreshchatyk St.'),
('Ivano-Frankivsk', 'Nezalezhnosti St.'),
('Uzhhorod', 'Korzo St.'),
('Poltava', 'Strytenska St.'),
('Zhytomyr', 'Peremohy St.'),
('Chernihiv', 'Shchorsa St.'),
('Vinnytsia', 'Soborna St.'),
('Chernivtsi', 'Holovna St.'),
('Kropyvnytskyi', 'Arsenichuka St.'),
('Rivne', 'Soborna St.');

INSERT INTO station (total_capacity, installation_date, location_id) VALUES
(5000.00, '2022-01-15', 1),
(7000.00, '2022-02-20', 2),
(3000.00, '2022-03-05', 3),
(2500.00, '2022-04-10', 4),
(8000.00, '2022-05-15', 5),
(6000.00, '2022-06-20', 6),
(4500.00, '2022-07-25', 7),
(7500.00, '2022-08-30', 8),
(9000.00, '2022-09-15', 9),
(5500.00, '2022-10-20', 10),
(3500.00, '2022-11-25', 11),
(9500.00, '2022-12-30', 12),
(4200.00, '2023-01-15', 13),
(6200.00, '2023-02-20', 14),
(7800.00, '2023-03-25', 15);

INSERT INTO solar_panel (installation_date, panel_type_id, station_id) VALUES
('2022-01-01', 3, 7),
('2022-01-10', 5, 9),
('2022-01-20', 7, 1),
('2022-02-01', 2, 6),
('2022-02-10', 6, 2),
('2022-02-20', 9, 8),
('2022-03-01', 7, 5),
('2022-03-10', 3, 4),
('2022-03-20', 6, 12),
('2022-04-01', 4, 11),
('2022-04-10', 13, 6),
('2022-04-20', 10, 4),
('2022-05-01', 5, 4),
('2022-05-10', 12, 13),
('2022-05-20', 15, 1);

INSERT INTO battery (capacity, installation_date, station_id) VALUES
('1000', '2022-01-05', 1),
('1200', '2022-02-10', 2),
('900', '2022-03-15', 6),
('1100', '2022-04-20', 4),
('1300', '2022-05-25', 8),
('1400', '2022-06-30', 6),
('1500', '2022-07-05', 5),
('1600', '2022-08-10', 8),
('1700', '2022-09-15', 9),
('1800', '2022-10-20', 10),
('1900', '2022-11-25', 4),
('2000', '2022-12-30', 1),
('2100', '2023-01-04', 6),
('2200', '2023-02-09', 2),
('2300', '2023-03-14', 15);

INSERT INTO battery_level (date_time, charge_level, battery_id) VALUES
('2022-01-05 10:00:00', 75.00, 1),
('2022-02-10 11:00:00', 80.00, 2),
('2022-03-15 12:00:00', 85.00, 3),
('2022-04-20 13:00:00', 70.00, 4),
('2022-05-25 14:00:00', 65.00, 5),
('2022-06-30 15:00:00', 60.00, 6),
('2022-07-05 16:00:00', 95.00, 7),
('2022-08-10 17:00:00', 90.00, 8),
('2022-09-15 18:00:00', 85.00, 9),
('2022-10-20 19:00:00', 80.00, 10),
('2022-11-25 20:00:00', 75.00, 11),
('2022-12-30 21:00:00', 70.00, 12),
('2023-01-04 22:00:00', 65.00, 13),
('2023-02-09 23:00:00', 60.00, 14),
('2023-03-14 00:00:00', 55.00, 15);

INSERT INTO panel_angle (date_time, angle, solar_panel_id) VALUES
('2022-01-01 10:00:00', 45.00, 1),
('2022-01-10 11:00:00', 50.00, 2),
('2022-01-20 12:00:00', 55.00, 3),
('2022-02-01 13:00:00', 60.00, 4),
('2022-02-10 14:00:00', 65.00, 5),
('2022-02-20 15:00:00', 70.00, 6),
('2022-03-01 16:00:00', 75.00, 7),
('2022-03-10 17:00:00', 80.00, 8),
('2022-03-20 18:00:00', 85.00, 9),
('2022-04-01 19:00:00', 90.00, 10),
('2022-04-10 20:00:00', 95.00, 11),
('2022-04-20 21:00:00', 100.00, 12),
('2022-05-01 22:00:00', 105.00, 13),
('2022-05-10 23:00:00', 110.00, 14),
('2022-05-20 00:00:00', 115.00, 15);

INSERT INTO panel_production (date_time, production, solar_panel_id) VALUES
('2022-01-01 10:00:00', 500.00, 1),
('2022-01-10 11:00:00', 600.00, 2),
('2022-01-20 12:00:00', 700.00, 3),
('2022-02-01 13:00:00', 800.00, 4),
('2022-02-10 14:00:00', 900.00, 5),
('2022-02-20 15:00:00', 1000.00, 6),
('2022-03-01 16:00:00', 1100.00, 7),
('2022-03-10 17:00:00', 1200.00, 8),
('2022-03-20 18:00:00', 1300.00, 9),
('2022-04-01 19:00:00', 1400.00, 10),
('2022-04-10 20:00:00', 1500.00, 11),
('2022-04-20 21:00:00', 1600.00, 12),
('2022-05-01 22:00:00', 1700.00, 13),
('2022-05-10 23:00:00', 1800.00, 14),
('2022-05-20 00:00:00', 1900.00, 15);

INSERT INTO `owner` (name, surname, contact_number) VALUES
('John', 'Doe', 123456789),
('Jane', 'Smith', 234567890),
('Michael', 'Johnson', 345678901),
('Emily', 'Davis', 456789012),
('David', 'Martinez', 567890123),
('Sarah', 'Lopez', 678901234),
('Chris', 'Brown', 789012345),
('Amanda', 'Wilson', 890123456),
('Brian', 'Taylor', 901234567),
('Lisa', 'Anderson', 102345678),
('Paul', 'Thomas', 112345678),
('Megan', 'Jackson', 122345678),
('Laura', 'White', 132345678),
('Daniel', 'Harris', 142345678),
('Emma', 'Martin', 152345678);

INSERT INTO owner_has_station (owner_id, station_id, ownership_percentage) VALUES
(1, 1, 50.00),
(2, 2, 75.00),
(3, 3, 100.00),
(6, 4, 60.00),
(5, 5, 80.00),
(6, 6, 90.00),
(10, 7, 70.00),
(8, 8, 85.00),
(2, 9, 65.00),
(10, 10, 55.00),
(5, 11, 50.00),
(12, 12, 45.00),
(5, 13, 95.00),
(14, 14, 100.00),
(15, 15, 75.00);

INSERT INTO energy_sale (energy_sold, price_per_kwh, date_time, station_id) VALUES
(100.50, 0.15, '2023-01-01 10:00:00', 1),
(200.75, 0.18, '2023-01-02 12:00:00', 2),
(150.60, 0.14, '2023-01-03 14:00:00', 3),
(175.80, 0.17, '2023-01-04 09:00:00', 4),
(180.30, 0.16, '2023-01-05 11:00:00', 5),
(190.25, 0.15, '2023-01-06 08:00:00', 6),
(210.45, 0.19, '2023-01-07 13:00:00', 7),
(220.70, 0.17, '2023-01-08 15:00:00', 8),
(230.95, 0.18, '2023-01-09 16:00:00', 9),
(240.10, 0.14, '2023-01-10 10:00:00', 10),
(250.35, 0.15, '2023-01-11 12:00:00', 11),
(260.40, 0.16, '2023-01-12 14:00:00', 12),
(270.55, 0.18, '2023-01-13 09:00:00', 13),
(280.75, 0.19, '2023-01-14 11:00:00', 14),
(290.90, 0.17, '2023-01-15 13:00:00', 15);

DROP PROCEDURE IF EXISTS get_solar_panels_after_panel_type;
DROP PROCEDURE IF EXISTS get_solar_panels_after_station;
DROP PROCEDURE IF EXISTS get_owners_after_station;
DROP PROCEDURE IF EXISTS get_stations_after_owner;
DROP PROCEDURE IF EXISTS get_batteries_after_station;

DELIMITER //

CREATE PROCEDURE get_solar_panels_after_panel_type(
		IN panel_type_id INT
	)
BEGIN
	SELECT pt.id panel_type_id, sp.id solar_panel_id, pt.type_name panel_type_name, pt.description panel_type_description
    FROM solar_panel sp
    JOIN panel_type pt ON sp.panel_type_id = pt.id
    WHERE sp.panel_type_id = panel_type_id;
END //

CREATE PROCEDURE get_solar_panels_after_station(
		IN station_id INT
	)
BEGIN
	SELECT s.id station_id, sp.id solar_panel_id,
    s.total_capacity station_total_capacity,
    s.installation_date station_installation_date,
    l.city station_location_city, l.street station_location_street
    FROM solar_panel sp
    JOIN station s ON sp.station_id = s.id
    JOIN location l ON s.location_id = l.id
    WHERE sp.station_id = station_id;
END //

CREATE PROCEDURE get_owners_after_station(
		IN station_id INT
	)
BEGIN
	SELECT ohs.id id, ohs.station_id, ohs.owner_id, o.name owner_name,
    o.surname owner_surname, o.contact_number owner_contact_number
    FROM owner o
    JOIN owner_has_station ohs ON o.id = ohs.owner_id
    WHERE ohs.station_id = station_id;
END //

CREATE PROCEDURE get_stations_after_owner(
		IN owner_id INT
	)
BEGIN
	SELECT ohs.id id, ohs.station_id, ohs.owner_id,
    s.total_capacity station_total_capacity,
    s.installation_date station_installation_date,
    l.city station_location_city, l.street station_location_street
    FROM station s
    JOIN owner_has_station ohs ON s.id = ohs.station_id
    JOIN location l ON s.location_id = l.id
    WHERE ohs.owner_id = owner_id;
END //

CREATE PROCEDURE get_batteries_after_station(
		IN station_id INT
	)
begin
	SELECT s.id station_id, b.id battery_id,
    s.total_capacity station_total_capacity,
    s.installation_date station_installation_date,
    l.city station_location_city, l.street station_location_street
    FROM battery b
    JOIN station s ON b.station_id = s.id
    JOIN location l ON s.location_id = l.id
    WHERE b.station_id = station_id;
end //

DELIMITER ;

