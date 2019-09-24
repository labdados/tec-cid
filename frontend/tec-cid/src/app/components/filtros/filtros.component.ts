import { Component, OnInit } from '@angular/core';
import { UnidadeGestora } from 'src/app/models/unidade-gestora.model';
import { MunicipiosService } from 'src/app/services/municipios.service';

@Component({
  selector: 'app-filtros',
  templateUrl: './filtros.component.html',
  styleUrls: ['./filtros.component.css']
})
export class FiltrosComponent implements OnInit {

  unidadeGestora: UnidadeGestora = null;
  codUnidadeGestora: string;
  exibir:boolean = false;

  public model: any;

  config = {
    displayKey: "NomeUnidadeGest", //if objects array passed which key to be displayed defaults to description
    search: true,
    limitTo: 10
  };

  constructor(
    private municipiosService: MunicipiosService
  ) { }

  ngOnInit() {
    this.municipiosService.getMunicipios()
  }

  get municipios() {
    return this.municipiosService.municipios
  }

  filtroUnidadeGestora(){
    this.codUnidadeGestora = this.unidadeGestora.CodUnidadeGest
    this.exibir = true;  
  }

}
