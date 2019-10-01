import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';
import { Licitacao } from '../models/licitacao.model';

@Injectable({
  providedIn: 'root'
})
export class LicitacaoService {

  constructor(
    private http: HttpClient
  ) { }

  getLicitacoesMunicipio(codUni?:any, ano?: any, tipoLic?: any){
    return this.http.get<any>(`${API_URL}/licitacoes?limite=20&pagina=${1}&ano=${ano}&codUni=${codUni}&tipoLic=${tipoLic}`)    
  }

  getLicitacao(idLicitacao:any) {
    return this.http.get<Licitacao>(`${API_URL}/licitacoes/${idLicitacao}`)
  }
}
