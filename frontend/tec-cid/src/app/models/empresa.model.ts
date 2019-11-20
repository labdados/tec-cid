export class Empresa {
    constructor (
        public cpf_cnpj_participante?: string,
        public n_licitacoes?: string,
        public n_participantes?: string,
        public nome_participante?: string,
        public valor_licitacoes?: string,
        public valor_propostas_vencedoras?: string,         
    ) {}
}
