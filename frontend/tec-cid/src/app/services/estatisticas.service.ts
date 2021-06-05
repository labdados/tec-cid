import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';
import { Observable } from 'rxjs';

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

  
  getDataMunicipios(numeroRanqueados):Observable<any>{
    return this.http.get<any>(`${API_URL}/estatisticas/licitacoes`, {
      params: {
        dataInicio: '2017-01-01',
        dataFim: '2020-12-31',
        agruparPor: 'municipio',
        limite: numeroRanqueados
      }
    })

  }

  getDataEmpresas(numeroRanqueados):Observable<any>{
    return this.http.get<any>(`${API_URL}/estatisticas/licitacoes`, {
      params: {
        dataInicio: '2017-01-01',
        dataFim: '2020-12-31',
        agruparPor: 'participante',
        limite: numeroRanqueados
      }
    })
  }
 
}
