import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Candidato } from '../models/candidato.model';
import {SERVER_URL} from '../shared/url/url.domain';

@Injectable({
  providedIn: 'root'
})
export class CandidatosService {

  candidato: Candidato;

  constructor(
    private http: HttpClient
  ) { }

  getCandidato(id_candidato: string) {
    return this.http.get<any>(`${SERVER_URL}/candidatos/${id_candidato}`).subscribe(res => {
      this.candidato = res.dados[0];
    });
  }
}
