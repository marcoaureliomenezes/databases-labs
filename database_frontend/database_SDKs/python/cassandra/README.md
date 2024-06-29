CREATE KEYSPACE employee
  WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};