import csv
from neo4j_utils import Neo4jUtils

CSV_NAME_AND_ID = '../../dados/summary/name_and_id.csv'
CSV_SIMPLE_RELATIONSHIP = '../../dados/summary/simple_relationships.csv'
CSV_OUTPUT_RESULTS = '../../dados/summary/summary.csv'

COUNT_INDEX = 0
NAME_INDEX = 0
ID_INDEX = 1

NODE_A_INDEX = 0
NODE_B_INDEX = 1
RELATIONSHIP_INDEX = 2
DIRECTIONALITY_INDEX = 3

neo4j_utils = Neo4jUtils()

def write_result(query, writer, label):
    result = neo4j_utils.get_query_response(query)
    writer.writerow([query.replace(";", ""), result[COUNT_INDEX][label]])
    total = result[COUNT_INDEX][label]
    print(f'{query.replace(";", "")}: {total}')


if __name__ == '__main__':
    neo4j_utils = Neo4jUtils()
    
    file = open(CSV_OUTPUT_RESULTS, 'w')
    writer = csv.writer(file, delimiter=",")
    writer.writerow(['query', 'result'])
    
    with open(CSV_NAME_AND_ID, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)

        for line in reader:
            node_name = line[NAME_INDEX]
            node_id = line[ID_INDEX]
            query = f"MATCH (n:{node_name}) RETURN COUNT(n.{node_id}) AS total;"

            write_result(query, writer, 'total')

    with open(CSV_SIMPLE_RELATIONSHIP, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)

        for line in reader:
            node_a = line[NODE_A_INDEX]
            node_b = line[NODE_B_INDEX]
            relationship = line[RELATIONSHIP_INDEX]
            directionality = line[DIRECTIONALITY_INDEX]
            query = 'MATCH x=(:' + node_a + ')-[:' + relationship + ']' + directionality + '(:' + node_b + ') RETURN COUNT(x) AS total;'

            write_result(query, writer, 'total')

    query = 'MATCH (n) RETURN COUNT(n) AS total;'
    write_result(query, writer, 'total')

    query = 'MATCH p=()-->() RETURN COUNT(p) AS total;'
    write_result(query, writer, 'total')

    file.close()