export class Licitacao {
    constructor(
        public ano_homologacao: string,
        public cd_modalidade: string,
        public cd_ugestora: string,
        public data_homologacao: string,        
        public id: string,
        public modalidade: string,
        public nome_estagio_processual: string,
        public nome_setor_atual: string,
        public numero_licitacao: string,
        public objeto: string,
        public situacao_fracassada: string,
        public url: string,
        public valor_estimado: string,
        public valor_licitado: string,
    ) {}
}