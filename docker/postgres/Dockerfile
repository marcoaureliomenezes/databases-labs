FROM postgres


COPY init_book_authors_db.sql /docker-entrypoint-initdb.d/
COPY init_montadoras_db.sql /docker-entrypoint-initdb.d/
COPY init_photos_score_db.sql /docker-entrypoint-initdb.d/
COPY init_celular_sales_db.sql /docker-entrypoint-initdb.d/
COPY init_user_product_order_db.sql /docker-entrypoint-initdb.d/