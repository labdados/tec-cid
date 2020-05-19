CALL apoc.periodic.commit(
    "MATCH p=(emp:Empenho)-[:GEROU]-(pag:Pagamento)-[:PARA]-(part:Participante)
        WITH p LIMIT {limit}
        DETACH DELETE p RETURN COUNT(*)",
        {limit:15000})
