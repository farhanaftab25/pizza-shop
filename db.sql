ALTER ROLE farhan SET client_encoding TO 'utf8';
ALTER ROLE farhan SET default_transaction_isolation TO 'read committed';
ALTER ROLE farhan SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE pizza TO farhan;