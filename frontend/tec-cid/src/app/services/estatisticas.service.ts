import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';

@Injectable({
  providedIn: 'root'
})
export class EstatisticasService {

  constructor(
    private http: HttpClient
  ) { }

  getEstatisticaMunicipio(id: string) {
    return this.http.get<any>(`${API_URL}/estatisticas/licitacoes`, {
      params: {
        idMunicipio: `${id}`,
        dataInicio: '2017-01-01',
        dataFim: '2020-12-31',
        agruparPor: 'municipio'
      }
    })
  }
}
