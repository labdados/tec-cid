import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {UnidadeGestora} from '../models/unidade-gestora.model';
import {SERVER_URL} from '../shared/url/url.domain';

@Injectable({
  providedIn: 'root'
})
export class UnidadeGestoraService {

  unidadesGestoras: UnidadeGestora[] = [];

  constructor(
    private http: HttpClient
  ) {
  }

  getUnidadesGestorasByMunicipio(municipio: string) {
    return this.http.get<any>(`${SERVER_URL}/unidades-gestoras`, {
      params: {
        nomeMunicipio: `${municipio}`
      }
    }).subscribe(res => {
      this.unidadesGestoras = res.dados;
    })
  }

}
