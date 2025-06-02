-- sql/db_schema.sql
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id SERIAL PRIMARY KEY,
    transaction_date DATE NOT NULL,
    description VARCHAR(255),
    amount DECIMAL(10, 2) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    -- category VARCHAR(100),
    -- transaction_type VARCHAR(100),
    currency VARCHAR(10) DEFAULT 'AUD'
);

-- Indexs for performance on frequently queried columns
CREATE INDEX IF NOT EXISTS idx_transaction_date ON transactions(transaction_date);
-- CREATE INDEX IF NOT EXISTS idx_category ON transactions(category);
-- CREATE INDEX IF NOT EXISTS idx_transaction_type ON transactions(transaction_type);
