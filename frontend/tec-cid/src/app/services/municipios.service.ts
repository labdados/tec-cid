import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { UnidadeGestora } from '../models/unidade-gestora.model';
import { API_URL } from './tc.api';

@Injectable({
  providedIn: 'root'
})
export class MunicipiosService {

  municipios: UnidadeGestora [];

  constructor(
    private http: HttpClient
  ) { }

  getMunicipios(){
    return this.http.get<UnidadeGestora[]>(`${API_URL}/unidades-gestoras`).subscribe(data => {
      this.municipios = data;
      console.log(data)
    })
  }

  getLicitacoesMunicipio(codUni:any){
    let ano = '';
    let tipoLic = '';
    return this.http.get<any>(`${API_URL}/licitacoes?limite=20&pagina=${1}&ano=${ano}&codUni=${codUni}&tipoLic=${tipoLic}`)    
  }
}
