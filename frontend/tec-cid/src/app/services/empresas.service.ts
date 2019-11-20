import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { API_URL } from './tc.api';
import { Empresa } from '../models/empresa.model';

@Injectable({
  providedIn: 'root'
})
export class EmpresasService {

  empresas: Empresa[];
  empresa: Empresa = new Empresa('', '', '', '', '', '')

  constructor(
    private http: HttpClient
  ) { }

  getLicitacoesEmpresa(idEmpresa: any, pagina: number) {
    return this.http.get<any>(`${API_URL}/participantes`,
      {
        params: {
          dataInicio: '2017-01-01',
          dataFim: '2020-12-31',
          limite: "9999",
          pagina: `${pagina}`,
          ordenarPor: 'valor_licitacoes',
          ordem: 'DESC',
          idEmpresa: `${idEmpresa}`
        }
      })
  }

}
