import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Empresa } from '../models/empresa.model';
import {SERVER_URL} from '../shared/url/url.domain';

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
    return this.http.get<any>(`${SERVER_URL}/participantes`,
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
