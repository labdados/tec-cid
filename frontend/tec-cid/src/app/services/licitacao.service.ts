import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';
import { Licitacao } from '../models/licitacao.model';
import { Proposta } from '../models/proposta.model';

@Injectable({
  providedIn: 'root'
})
export class LicitacaoService {

  propostas: Proposta[] = []
  vencedores: boolean;
  perdedores: boolean;
  exibirPerdedores: boolean;

  constructor(
    private http: HttpClient
  ) { }

  getLicitacoesMunicipio(codUni?:any, ano?: any, tipoLic?: any){
    return this.http.get<any>(`${API_URL}/licitacoes?limite=40&pagina=${1}&ano=${ano}&codUni=${codUni}&tipoLic=${tipoLic}`)    
  }

  getLicitacao(idLicitacao:any) {
    return this.http.get<any>(`${API_URL}/licitacoes/${idLicitacao}`)
  }

  getPropostas(idLicitacao:string) {
    return this.http.get<any>(`${API_URL}/licitacoes/${idLicitacao}/propostas`).subscribe(res => {
      this.propostas = res.dados;
      this.verificacao();
    })
  }

  verificacao() {
    let venc = 0;
    let perd = 0;
    this.propostas.forEach(e => {
      if (e.situacao_proposta == 'Vencedora') {
        venc++;
      } else if (e.situacao_proposta == 'Perdedora') {
        perd++;
      }
    });

    if(venc > 1) {
      this.vencedores = true;
    } else {
      this.vencedores = false;
    }

    if (perd > 1) {
      this.perdedores = true;
    } else if (perd == 0) {
      this.perdedores = false;
      this.exibirPerdedores = true;
    }

  }
}
