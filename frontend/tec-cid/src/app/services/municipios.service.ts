import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {Municipio} from '../models/municipio.model';
import {SERVER_URL} from '../shared/url/url.domain';

@Injectable({
  providedIn: 'root'
})
export class MunicipiosService {

  municipios: Municipio[];
  municipio: Municipio;

  constructor(
    private http: HttpClient
  ) {
  }

  getMunicipios() {
    return this.http.get<any>(`${SERVER_URL}/municipios`,
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
    return this.http.get<any>(`${SERVER_URL}/licitacoes`,
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
  }

  getMunicipio(id: string) {
    return this.http.get<any>(`${SERVER_URL}/municipios/${id}`).subscribe(res => {
      this.municipio = res.dados[0];
    })
  }

  getGestao(id: string, ano: number) {
    return this.http.get<any>(`${SERVER_URL}/municipios/${id}/gestoes`, {
      params: {
        ano: `${ano}`
      }
    })
  }

}
