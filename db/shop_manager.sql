DROP TABLE IF EXISTS inventory_items;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    established INT
);

CREATE TABLE inventory_items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_cost INT,
    selling_price INT
);

