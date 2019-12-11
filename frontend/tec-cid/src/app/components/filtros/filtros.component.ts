import { Component, OnInit, ElementRef, AfterViewInit } from '@angular/core';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Municipio } from 'src/app/models/municipio.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';
import { Router } from '@angular/router';
import { Gestao } from 'src/app/models/gestao.model';
import { CandidatosService } from 'src/app/services/candidatos.service';
import {UnidadeGestoraService} from "../../services/unidade-gestora.service";

@Component({
  selector: 'app-filtros',
  templateUrl: './filtros.component.html',
  styleUrls: ['./filtros.component.css']
})
export class FiltrosComponent implements OnInit, AfterViewInit {

  exibir: boolean = false;
  cidade: Municipio;
  valorLicitacoes: any;
  gestao: Gestao;
  isLoadingResults: boolean = false;

  configCidades = {
    displayKey: "nome",
    search: true,
    limitTo: 10,
    placeholder: 'Selecione um município',
    noResultsFound: 'Nenhum município encontrado',
    searchPlaceholder: 'Buscar',
    searchOnKey: 'nome'
  };

  constructor(
    private municipiosService: MunicipiosService,
    private unidadeGestoraService: UnidadeGestoraService,
    private estatisticasService: EstatisticasService,
    private candidatosService: CandidatosService,
    private router: Router,
    private elementRef: ElementRef
  ) { }

  ngOnInit() {
    this.municipiosService.getMunicipios();
  }

  ngAfterViewInit() {
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = '#F5F5F5';
  }

  get municipios() {
    return this.municipiosService.municipios;
  }

  get municipio() {
    return this.municipiosService.municipio;
  }

  get unidadesGestoras() {
    return this.unidadeGestoraService.unidadesGestoras;
  }

  get candidato() {
    return this.candidatosService.candidato;
  }

  displayFn(municipio?: Municipio): string | undefined {
    return municipio ? municipio.nome : undefined;
  }

  filtroMunicipio() {
    this.isLoadingResults = true;
    this.municipiosService.getMunicipio(this.cidade.id);
    this.getValorLicitacoes(this.cidade.id);
    this.getGestao();
    this.unidadeGestoraService.getUnidadesGestorasByMunicipio(this.cidade.nome);
    setTimeout(() => {
      this.isLoadingResults = false;
      this.show();
    }, 2000);
  }

  show() {
    if (this.municipio === undefined || this.gestao === undefined || this.candidato === undefined) {
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
