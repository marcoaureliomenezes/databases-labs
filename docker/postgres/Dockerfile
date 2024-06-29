FROM postgres


COPY ./databases/sucos_vendas/sucos_dadaia_schema.sql /docker-entrypoint-initdb.d/
COPY ./databases/company/company_dadaia_schema.sql /docker-entrypoint-initdb.d/
COPY ./databases/learning/sharding.sql /docker-entrypoint-initdb.d/



COPY ./databases/sucos_vendas/sucos_dadaia_data.sql /seeders/sucos_dadaia_data.sql
COPY ./databases/company/company_dadaia_data.sql /seeders/company_dadaia_data.sql
