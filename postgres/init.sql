SELECT 'CREATE DATABASE api_graphql'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'arch_spring')\gexec

\c api_graphql;