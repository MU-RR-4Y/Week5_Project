DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS destinations;

CREATE TABLE destinations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    information VARCHAR(255)
 );

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    destination_id INT NOT NULL REFERENCES destinations(id) ON DELETE CASCADE
    
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    wish_list INT NOT NULL REFERENCES destinations(id) ON DELETE CASCADE,
    vistied_list INT NOT NULL REFERENCES destinations(id) ON DELETE CASCADE
);

CREATE TABLE visits(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    destination_id INT NOT NULL REFERENCES destinations(id) ON DELETE CASCADE,
    date VARCHAR(225),
    rating INT,
    comment VARCHAR(255)

);
