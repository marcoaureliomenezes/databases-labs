current_branch = 1.0.0


deploy_single_postgres:
	docker-compose -f services/postgres/single_node.yml up -d


stop_single_postgres:
	docker-compose -f services/postgres/single_node.yml down