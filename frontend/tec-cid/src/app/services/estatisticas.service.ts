import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {SERVER_URL} from '../shared/url/url.domain';

@Injectable({
  providedIn: 'root'
})
export class EstatisticasService {

  constructor(
    private http: HttpClient
  ) { }

  getEstatisticaMunicipio(id: string) {
    return this.http.get<any>(`${SERVER_URL}/estatisticas/licitacoes`, {
      params: {
        idMunicipio: `${id}`,
        dataInicio: '2017-01-01',
        dataFim: '2020-12-31',
        agruparPor: 'municipio'
      }
    })
  }

  getRankingMunicipios(topN) {
    return this.http.get<any>(`${SERVER_URL}/estatisticas/licitacoes`, {
      params: {
        dataInicio: '2017-01-01',
        dataFim: '2020-12-31',
        agruparPor: 'municipio',
        limite: topN
      }
    })
  }

  getRankingEmpresas(topN) {
    return this.http.get<any>(`${SERVER_URL}/estatisticas/licitacoes`, {
      params: {
        dataInicio: '2017-01-01',
        dataFim: '2020-12-31',
        agruparPor: 'participante',
        limite: topN
      }
    })
  }
}
