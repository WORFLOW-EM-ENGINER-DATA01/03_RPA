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



