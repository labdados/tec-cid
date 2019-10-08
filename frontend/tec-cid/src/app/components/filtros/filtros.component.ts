import { Component, OnInit } from '@angular/core';
import { UnidadeGestora } from 'src/app/models/unidade-gestora.model';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Municipio } from 'src/app/models/municipio.model';
import { UnidadeGestoraService } from 'src/app/services/unidade-gestora.service';

@Component({
  selector: 'app-filtros',
  templateUrl: './filtros.component.html',
  styleUrls: ['./filtros.component.css']
})
export class FiltrosComponent implements OnInit {

  exibir:boolean = false;
  cidade: Municipio;
  unidadeGestora: UnidadeGestora;
  lista: string[] = [];

  public model: any;

  configCidades = {
    displayKey: "nome",
    search: true,
    limitTo: 10,
    placeholder: 'Selecione seu município',
    noResultsFound: 'Nenhum município encontrado',
    searchPlaceholder:'Buscar',
    searchOnKey: 'nome'
  };

  configUnidadesGestoras = {
    displayKey: "nome",
    limitTo: 10,
    placeholder: 'Selecione a unidade gestora',
  };

  constructor(
    private municipiosService: MunicipiosService,
    private unidadeGestoraService: UnidadeGestoraService
  ) { }

  ngOnInit() {
    this.municipiosService.getMunicipios();
  }

  get municipios() {
    return this.municipiosService.municipios
  }

  get municipio() {
    return this.municipiosService.municipio
  }

  get unidadesGestoras() {
    return this.unidadeGestoraService.unidadesGestoras
  }

  filtroMunicipio(){
    this.show();
    this.municipiosService.getMunicipio(this.cidade.id);
    this.unidadeGestoraService.getUnidadesGestorasByMunicipio(this.cidade.nome)
  }

  show() {
    if (this.municipio == null || this.municipio == undefined || this.municipio == ''){
      this.exibir = false;
      return true;
    } else {
      this.exibir = true;
      return false;
    }
  }

}
