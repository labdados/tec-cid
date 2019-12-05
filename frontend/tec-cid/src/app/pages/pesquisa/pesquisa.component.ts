import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
//import { DataModel } from 'src/app/models/data.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';
import { NgxSpinnerService } from "ngx-spinner";


@Component({
  selector: 'app-pesquisa',
  templateUrl: './pesquisa.component.html',
  styleUrls: ['./pesquisa.component.css']
})
export class PesquisaComponent implements OnInit {

  data: Observable<any>;
  dataEmpresas: Observable<any>;

  constructor(private http: HttpClient, private estatisticasService: EstatisticasService) {
    this.estatisticasService.getRankingMunicipios(10).subscribe(res => {
      this.data = res.dados;
    })
    this.estatisticasService.getRankingEmpresas(10).subscribe(res => {
      this.dataEmpresas = res.dados;
    })
  }

  ngOnInit() {
  }

}

class SpinnerComponent implements OnInit {
  constructor(private spinner: NgxSpinnerService) {}
 
  ngOnInit() {
    /** spinner starts on init */
    this.spinner.show();
 
    setTimeout(() => {
      /** spinner ends after 5 seconds */
      this.spinner.hide();
    }, 5000);
  }
}
