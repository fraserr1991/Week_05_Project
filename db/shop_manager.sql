DROP TABLE IF EXISTS inventory_items;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN,
    established INT
);

CREATE TABLE inventory_items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_cost FLOAT,
    selling_price FLOAT,
    image VARCHAR(255),
    manufacturer_id INT NOT NULL REFERENCES manufacturers(id) ON DELETE CASCADE
);

