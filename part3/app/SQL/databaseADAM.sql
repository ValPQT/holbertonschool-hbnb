/* Initial Data for HBNB */

/* -------- ADMIN USER -------- */
INSERT INTO users (id, email, first_name, last_name, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'admin@hbnb.io',
    'Admin',
    'HBnB',
    '$2b$12$KIX1y4zL6Q6G9yC1nH4nXu0v.yhUk7Q8tSvy1K9yKQzXj1a9R2N3G',
    TRUE
);

/* -------- AMENITIES -------- */
INSERT INTO amenities (id, name) VALUES
('a1f0d6e5-9e12-4b3a-bfd7-1a2e5c3f8d12', 'WiFi'),
('b2e1c7f3-3d45-4f2b-91ae-8b7d9c1e0f34', 'Swimming Pool'),
('c3f2d8a4-6a78-4d1c-ae9b-3d2f4b5e7a89', 'Air Conditioning');
