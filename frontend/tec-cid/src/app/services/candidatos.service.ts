import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './tc.api';
import { Candidato } from '../models/candidato.model';

@Injectable({
  providedIn: 'root'
})
export class CandidatosService {

  candidato: Candidato;

  constructor(
    private http: HttpClient
  ) { }

  getCandidato(id_candidato: string) {
    return this.http.get<any>(`${API_URL}/candidatos/${id_candidato}`).subscribe(res => {
      this.candidato = res.dados[0];
    });
  }
}
