import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { UnidadeGestora } from '../models/unidade-gestora.model';
import { API_URL } from './tc.api';
import { Municipio } from '../models/municipio.model';
import { identifierModuleUrl } from '@angular/compiler';

@Injectable({
  providedIn: 'root'
})
export class MunicipiosService {

  // municipios: UnidadeGestora [];
  // unidadesGestoras: UnidadeGestora [] = [];
  municipios: Municipio[];
  municipio: Municipio;

  constructor(
    private http: HttpClient
  ) { }

  getMunicipios(){
    return this.http.get<any>(`${API_URL}/municipios`, 
    {
      params: 
      {
        campos: 'id,nome',
        pagina: '1',
        limite: '230'
      }
    }).subscribe(data => {
      this.municipios = data.dados;
    })
  }

  getLicitacoesMunicipio(codUni:any, ano: any, tipoLic: any, pagina:number){
    return this.http.get<any>(`${API_URL}/licitacoes`, 
    {
      params: {
        limite: "10",
        pagina: `${pagina}`,
        codUni: `${codUni}`,
        tipoLic: `${tipoLic}`,
        ordenarPor: 'data_homologacao',
        ordem: 'DESC'
      }
    })    

    // return this.http.get<any>(`${API_URL}/licitacoes?limite=10&pagina=${pagina}&ano=${ano}&codUni=${codUni}&tipoLic=${tipoLic}`)    
  }

  getMunicipio(id:string) {
    return this.http.get<any>(`${API_URL}/municipios/${id}`).subscribe(res => {
      this.municipio = res.dados[0];
    })
  }

}
