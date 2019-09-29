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
  cidade: string;
  lista: string[] = [];

  public model: any;

  configCidades = {
    displayKey: "Cidades",
    search: true,
    limitTo: 10,
    placeholder: 'Selecione seu município',
    noResultsFound: 'Nenhum município encontrado',
    searchPlaceholder:'Buscar'
  };

  configUnidadesGestoras = {
    displayKey: "NomeUnidadeGest",
    // search: true,
    limitTo: 10,
    placeholder: 'Selecione a unidade gestora',
    // noResultsFound: 'Nenhum município encontrado',
    // searchPlaceholder:'Buscar'
  };

  constructor(
    private municipiosService: MunicipiosService
  ) { }

  ngOnInit() {
    this.municipiosService.getCidades();
    this.municipiosService.getMunicipios();
  }

  get municipios() {
    return this.municipiosService.cidades
  }

  get unidadesGestoras() {
    return this.municipiosService.municipios
  }

  filtroUnidadeGestora(){
    this.codUnidadeGestora = this.unidadeGestora.CodUnidadeGest
    this.exibir = true;  
  }

  filtroCidade(){
    this.show();
    this.municipiosService.filter(this.cidade.toLowerCase())
  }

  getUnidadeGestora() {
    if (this.unidadeGestora != null || this.unidadeGestora != undefined){
      this.codUnidadeGestora = this.unidadeGestora.CodUnidadeGest
    }
  }

  show() {
    if (this.cidade == null || this.cidade == undefined || this.cidade == ''){
      this.exibir = false;
      return true;
    } else {
      this.exibir = true;
      return false;
    }
  }

}
