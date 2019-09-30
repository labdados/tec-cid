import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';

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
}
