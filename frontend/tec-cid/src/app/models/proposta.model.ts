export class Proposta {
    constructor (
        public cd_modalidade_licitacao: string,
        public cd_ugestora: string,
        public cpf_cnpj_participante: string,
        public nome_participante: string,
        public numero_licitacao: string,
        public situacao_proposta: string,
        public valor_proposta: string
    ) {}
}