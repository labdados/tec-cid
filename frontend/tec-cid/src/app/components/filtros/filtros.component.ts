import { Component, OnInit } from '@angular/core';
import { UnidadeGestora } from 'src/app/models/unidade-gestora.model';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Municipio } from 'src/app/models/municipio.model';
import { UnidadeGestoraService } from 'src/app/services/unidade-gestora.service';
import { EstatisticasService } from 'src/app/services/estatisticas.service';
import { Router } from '@angular/router';
import { Gestao } from 'src/app/models/gestao.model';
import { CandidatosService } from 'src/app/services/candidatos.service';
import { Candidato } from 'src/app/models/candidato.model';

@Component({
  selector: 'app-filtros',
  templateUrl: './filtros.component.html',
  styleUrls: ['./filtros.component.css']
})
export class FiltrosComponent implements OnInit {

  exibir:boolean = false;
  mostrar:boolean = false;
  cidade: Municipio;
  unidadeGestora: any;
  lista: string[] = [];
  valorLicitacoes: any;
  gestao: Gestao;

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
  }

  constructor(
    private municipiosService: MunicipiosService,
    private unidadeGestoraService: UnidadeGestoraService,
    private estatisticasService: EstatisticasService,
    private candidatosService: CandidatosService,
    private router: Router
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

  get candidato() {
    return this.candidatosService.candidato
  }

  filtroMunicipio(){
    this.municipiosService.getMunicipio(this.cidade.id);
    this.getValorLicitacoes(this.cidade.id);
    this.getGestao();
    this.unidadeGestoraService.getUnidadesGestorasByMunicipio(this.cidade.nome);
    this.show();
  }

  show() {
    if (this.municipio === undefined || this.gestao === undefined || this.candidato === undefined){
      this.exibir = false;
    } else {
      this.exibir = true;
    }
  }

  getValorLicitacoes(id: string) {
    this.estatisticasService.getEstatisticaMunicipio(id).subscribe(res => {
      this.valorLicitacoes = res.dados[0].valor_licitacoes
    })
  }

  getGestao() {
    let ano = new Date().getFullYear();
    this.municipiosService.getGestao(this.cidade.id, ano).subscribe(res => {
      this.gestao = res.dados[0];
      
      this.candidatosService.getCandidato(this.gestao.id_candidato);
    })
    console.log(this.gestao)
  }

  exibirMunicipio() {
    this.router.navigate(['/municipio', this.cidade.id])
  }

}
