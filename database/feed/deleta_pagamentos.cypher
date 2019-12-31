CALL apoc.periodic.commit(
    "MATCH (p:Pagamento) 
        WITH p LIMIT {limit} 
        DETACH DELETE p RETURN COUNT(*)", 
        {limit:15000})