\c db

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(10) NOT NULL,
    client VARCHAR(100) NOT NULL,
    amount_ht DECIMAL(10, 2) NOT NULL,
    hours_count INTEGER NOT NULL,
    days_count INTEGER NOT NULL,
    trainer VARCHAR(100) NOT NULL,
    trainer_shortcode VARCHAR(50) NOT NULL,
    payment_due VARCHAR(50) NOT NULL,
    intervention_dates JSONB
) ;

-- Création des écoles
CREATE TABLE schools (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO schools (name) VALUES 
('Computer School'),
('ESIT'),
('EIT'),
('The Bridge');

-- Création des formateurs
CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    shortcode VARCHAR(50) NOT NULL
);

INSERT INTO trainers (name, shortcode) VALUES 
('Lucie Bouvier', 'LB01'),
('Margot Caron', 'MC01'),
('Théophile Sauvage', 'TS01'),
('Susan Fernandes', 'SF01'),
('Danielle Chevallier', 'DC01'),
('Martine Roger', 'MR01'),
('Clémence Auger', 'CA01'),
('Franck Riou', 'FR01'),
('Joséphine Joseph', 'JJ01'),
('Claude Garcia', 'CG01');

-- Génération des factures



INSERT INTO invoices (
    invoice_number, client, amount_ht, hours_count, days_count, 
    trainer, trainer_shortcode, payment_due, intervention_dates
)
SELECT 
    '0000' || i AS invoice_number,
    CASE 
        WHEN i % 4 = 0 THEN 'Computer School'
        WHEN i % 4 = 1 THEN 'ESIT'
        WHEN i % 4 = 2 THEN 'EIT'
        WHEN i % 4 = 3 THEN 'The Bridge'
    END AS client,
    ROUND((RANDOM() * 2000 + 500)::numeric, 2) AS amount_ht,  -- Corrected rounding syntax
    ROUND(RANDOM() * 80 + 10)::integer AS hours_count,  -- Ensure integer type
    ROUND(5)::integer AS days_count,  -- Ensure integer type
        (
            SELECT name FROM trainers ORDER BY RANDOM() LIMIT 1
        ) AS trainer,
        (
            SELECT shortcode FROM trainers ORDER BY RANDOM() LIMIT 1
        ) AS trainer_shortcode,
    'Payment due: ' || (ROUND(RANDOM() * 60 + 15))::integer || ' days' AS payment_due,  -- Ensure integer type
       jsonb_build_object(
        'start_date', to_char(
            DATE '2023-01-01' + ((i - 1) / 10 * INTERVAL '1 MONTH') + ((i - 1) % 10 * 3 || ' days')::INTERVAL, 
            'YYYY-MM-DD'
        ),
        'end_date', to_char(
            DATE '2023-01-01' + ((i - 1) / 10 * INTERVAL '1 MONTH') + ((i - 1) % 10 * 3 || ' days')::INTERVAL + INTERVAL '5 days', 
            'YYYY-MM-DD'
        )
    ) AS intervention_dates
FROM generate_series(1, 120) AS s(i);