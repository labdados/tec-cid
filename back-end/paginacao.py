class Paginacao:
    def __init__(self, dao):
        self.page_atual_lic = 1
        self.page_atual_part = 1

        self.repo_licitacoes = []
        self.repo_participantes = []

        self.dao = dao

    def get_licitacoes(self, page, limit, tipo):
        
        print("page: ", page)
        print("self.page: ", self.page_atual_lic)

        # Indo para o próximo resultado
        if page > self.page_atual_lic:
            print("proximo page: {}", page)
            self.page_atual_lic = page
            try:
                return self.repo_licitacoes[page-1]
            except IndexError:
                print("entrou no except")
                result = self.dao.get_licitacoes(limit)
                #result = self.proximo(tipo, limit)
                self.repo_licitacoes.append(result)
                print("tamanho do repositorio: ",len(self.repo_licitacoes))
                return result

        # Indo para o resultado anterior
        elif page < self.page_atual_lic:
            print("anterior page: {}", page)
            self.page_atual_lic = page
            print("tamanho do repositorio: ",len(self.repo_licitacoes))
            return self.repo_licitacoes[page-1]
        
        # Indo para o resultado inicial
        elif page == 1:
            print("atual page: {}", page)
            self.page_atual_lic = page
            try:
                return self.repo_licitacoes[0]
            except IndexError:
                result = self.dao.get_licitacoes(limit)
                #result = self.start(tipo, limit)
                self.repo_licitacoes.append(result)
                print("tamanho do repositorio: ",len(self.repo_licitacoes))
                return result
        
        # Recarregando a mesma página
        elif page == self.page_atual_lic:
            print("same page: {}", page)
            return self.repo_licitacoes[page-1]

    
    def get_participantes(self, page, limit, tipo):
        
        # Indo para a próxima página
        if page > self.page_atual_part:
            self.page_atual_part = page
            try:
                return self.repo_participantes[page-1]
            except IndexError:
                result = self.dao.get_participantes(limit)
                #result = self.proximo(tipo, limit)
                self.repo_participantes.append(result)
                return result
        
        # Indo para a página anterior
        elif page < self.page_atual_part:
            self.page_atual_part = page
            return self.repo_participantes[page-1]
        
        # Indo para a primeira página
        elif page == 1:
            print("atual page: {}", page)
            self.page_atual_part = page
            try:
                return self.repo_participantes[0]
            except IndexError:
                result = self.dao.get_participantes(limit)
                #result = self.start(tipo, limit)
                self.repo_participantes.append(result)
                print("tamanho do repositorio: ",len(self.repo_participantes))
                return result
        
        # Recarregando a mesma página
        elif page == self.page_atual_part:
            print("same page: {}", page)
            return self.repo_participantes[page-1]
            