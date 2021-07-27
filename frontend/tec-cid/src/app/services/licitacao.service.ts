import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';
import { Licitacao } from '../models/licitacao.model';
import { Proposta } from '../models/proposta.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LicitacaoService {

  propostas: Proposta[] = []
  vencedores: boolean;
  perdedores: boolean;
  licitacao: Licitacao = new Licitacao('', '', '', '', '', '', '', '', '', '', '', '', '', ' ', ' ')
  constructor(
    private http: HttpClient
  ) { }
  
  
  getLicitacoesMunicipio(idMunicipio?: any, codUni?:any, anoInicio?: any,anoFim?:any, tipoLic?: any){
    return this.http.get<any>(`${API_URL}/licitacoes?limite=40&pagina=${1}&ano=${anoInicio}&codUni=${codUni}&tipoLic=${tipoLic}&idMunicipio=${idMunicipio}`)    
  }

  getLicitacao(idLicitacao:any): Observable<any> {
    return this.http.get<any>(`${API_URL}/licitacoes/${idLicitacao}`)
  }

  getPropostas(idLicitacao:string) {
    return this.http.get<any>(`${API_URL}/licitacoes/${idLicitacao}/propostas`).subscribe(res => {
      this.propostas = res.dados;
      this.Nova_verificacao();
    })
  }

  Nova_verificacao(){
    this.propostas.forEach( elemento => { 
      if(elemento.situacao_proposta == "Perdedora") return this.perdedores = true   
      else return this.perdedores = false  
    })
  }

  
}
