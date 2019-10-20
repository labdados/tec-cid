export class Candidato {
    constructor(
        public ano_eleicao: number,
        public cargo: string,
        public cd_eleicao: string,
        public coligacao: string,
        public cpf: string,
        public genero: string,
        public grau_instrucao: string,
        public id: string,
        public municipio: string,
        public nome: string,
        public nome_urna: string,
        public numero: string,
        public ocupacao: string,
        public raca: string,
        public sigla_partido: string,
        public situacao: string,
        public uf: string,        
    ) {}
}