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
  municipio: Municipio = new Municipio('', '', '', '', '', '', '', '', '', '', '', '', '')

  constructor(
    private http: HttpClient
  ) { }

  getMunicipios(){
    return this.http.get<any>(`${API_URL}/municipios`, 
    {
      params: 
      {
        atributos: 'id,nome',
        pagina: '1',
        limite: '230'
      }
    }).subscribe(data => {
      this.municipios = data.dados;
    })
  }

  getLicitacoesMunicipio(idMunicipio:any, ano: any, tipoLic: any, pagina:number){
    return this.http.get<any>(`${API_URL}/licitacoes`, 
    {
      params: {
        tipoLic: `${tipoLic}`,
        dataInicio: '2017-01-01',
        dataFim: '2020-12-31',
        limite: "10",
        pagina: `${pagina}`,
        ordenarPor: 'data_homologacao',
        ordem: 'DESC',
        idMunicipio: `${idMunicipio}`
      }
    })    

    // return this.http.get<any>(`${API_URL}/licitacoes?limite=10&pagina=${pagina}&ano=${ano}&codUni=${codUni}&tipoLic=${tipoLic}`)    
  }

  getMunicipio(id:string) {
    return this.http.get<any>(`${API_URL}/municipios/${id}`).subscribe(res => {
      this.municipio = res.dados[0];
    })
  }

  getGestao(id: string, ano:number) {
    return this.http.get<any>(`${API_URL}/municipios/${id}/gestoes`, {
      params: {
        ano: `${ano}`
      }
    })
  }

}
