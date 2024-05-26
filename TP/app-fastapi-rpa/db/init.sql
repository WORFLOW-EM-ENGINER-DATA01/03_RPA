\c db

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(10) NOT NULL,
    client VARCHAR(100) NOT NULL,
    amount_ht DECIMAL(10, 2) NOT NULL,
    hours_count INTEGER NOT NULL,
    days_count INTEGER NOT NULL,
    trainer VARCHAR(100) NOT NULL,
    trainer_shorcode VARCHAR(50) NOT NULL,
    payment_due VARCHAR(50) NOT NULL
);

CREATE TABLE intervention_dates (
    id SERIAL PRIMARY KEY,
    invoice_id INTEGER REFERENCES invoices(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

DO $$
DECLARE
    json_data JSON;
BEGIN
    json_data := pg_read_file('invoices.json');
    
    -- Insérer les données JSON dans la table invoices
    INSERT INTO invoices (invoice_number, client, amount_ht, hours_count, days_count, trainer, payment_due)
    SELECT
        (item->>'Facture n°')::VARCHAR,
        (item->>'Client')::VARCHAR,
        (regexp_replace(item->>'Montant HT', ' euro', '', 'g'))::DECIMAL,
        (item->>'Nombres d''heures')::INTEGER,
        (item->>'Nombre de jours')::INTEGER,
        (item->>'Formateur')::VARCHAR,
        (item->>'Payer à')::VARCHAR
    FROM
        json_array_elements(json_data) AS item;
END $$;

-- Lire les données JSON depuis le fichier et les insérer dans la table intervention_dates
DO $$
DECLARE
    json_data JSON;
BEGIN
    -- Lire le fichier JSON et le stocker dans la variable json_data
    json_data := pg_read_file('invoices.json');
    
    -- Insérer les données JSON dans la table intervention_dates
    INSERT INTO intervention_dates (invoice_id, start_date, end_date)
    SELECT
        invoices.id,
        (item->'Dates d''interventions'->>'Date début')::DATE,
        (item->'Dates d''interventions'->>'Date fin')::DATE
    FROM
        invoices,
        json_array_elements(json_data) AS item
    WHERE
        invoices.invoice_number = (item->>'Facture n°')::VARCHAR;
END $$;
