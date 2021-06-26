import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';
import { Municipio } from 'src/app/models/municipio.model';
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
//http://labdados.dcx.ufpb.br/tec-cid/api/licitacoes?limite=1&pagina=1&idMunicipio=1368
  public  ReqMunicipios():Observable<any>{
    return this.http.get<any>(`${API_URL}/municipios`,{
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

  geraStringData(data){
      return data.ano+"-" + data.mes +"-"+ data.dia
  }

  getLicitacoesMunicipio(idMunicipio: any, pagina: number, dataInicio:any, dataFim:any) {
    let dataInicial;
    let dataFinal;
    if(dataInicio !== '2017-01-01' && dataFim !== '2020-12-31'){
        dataInicial = this.geraStringData(dataInicio)
        dataFinal = this.geraStringData(dataFim)
    }else{
      dataInicial = dataInicio
      dataFinal = dataFim
    }
    return this.http.get<any>(`${API_URL}/licitacoes`,
      {
        params: {
          dataInicio: dataInicial,
          dataFim: dataFinal,
          limite: "200",
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
