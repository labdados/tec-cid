import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
//import { DataModel } from 'src/app/models/data.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';

@Component({
  selector: 'app-pesquisa',
  templateUrl: './pesquisa.component.html',
  styleUrls: ['./pesquisa.component.css']
})
export class PesquisaComponent implements OnInit {

  data: Observable<any>;

  constructor(private http: HttpClient, private estatisticasService: EstatisticasService) {
    this.estatisticasService.getRankingMunicipios(10).subscribe(res => {
      this.data = res.dados;
    })
  }

  ngOnInit() {
  }

}
