import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';
import { Municipio } from '../models/municipio.model';
import {Observable} from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class MunicipiosService {

  municipios: Municipio[];
  municipio: Municipio = new Municipio('', '', '', '', '', '', '', '', '', '', '', '', '')

  constructor(
    private http: HttpClient
  ) { }

  public teste():Observable<any>{
    return this.http.get<any>('http://labdados.dcx.ufpb.br/tec-cid/api/municipios',{
        params:{
          atributos: 'id,nome',
          pagina: '1',
          limite: '230'
        }
    })
  }
  getMunicipios() {
    return this.http.get<any>(`${API_URL}/municipios`,
      {
        params:
        {
          atributos: 'id,nome',
          pagina: '1',
          limite: '230'
        }
      }).subscribe(res => { 
        this.municipios = res.dados
      })
  }

  getLicitacoesMunicipio(idMunicipio: any, pagina: number) {
    return this.http.get<any>(`${API_URL}/licitacoes`,
      {
        params: {
          dataInicio: '2017-01-01',
          dataFim: '2020-12-31',
          limite: "9999",
          pagina: `${pagina}`,
          ordenarPor: 'data_homologacao',
          ordem: 'DESC',
          idMunicipio: `${idMunicipio}`
        }
      })

    // return this.http.get<any>(`${API_URL}/licitacoes?limite=10&pagina=${pagina}&ano=${ano}&codUni=${codUni}&tipoLic=${tipoLic}`)    
  }

  getMunicipio(id: string) {
    return this.http.get<any>(`${API_URL}/municipios/${id}`).subscribe(res => {
      this.municipio = res.dados[0];
    })
  }

  getGestao(id: string, ano: number) {
    return this.http.get<any>(`${API_URL}/municipios/${id}/gestoes`, {
      params: {
        ano: `${ano}`
      }
    })
  }

}
