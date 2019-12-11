import { Component, OnInit, ElementRef, AfterContentInit, AfterViewInit } from '@angular/core';
import { UnidadeGestora } from 'src/app/models/unidade-gestora.model';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Licitacao } from 'src/app/models/licitacao.model';
import { CandidatosService } from 'src/app/services/candidatos.service';
import { Gestao } from 'src/app/models/gestao.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';

@Component({
  selector: 'app-municipio',
  templateUrl: './municipio.component.html',
  styleUrls: ['./municipio.component.css']
})
export class MunicipioComponent implements OnInit, AfterViewInit {

  idMunicipio: any;
  tipoLic: any = '';
  codTipoLic: string = '';
  gestao: Gestao;
  valor_total_licitacoes: any = '';

  constructor(
    private route: ActivatedRoute,
    private municipioService: MunicipiosService,
    private candidatosService: CandidatosService,
    private estatisticasService: EstatisticasService,
    private elementRef: ElementRef
  ) { }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => this.idMunicipio = params['idMunicipio']);

    this.municipioService.getMunicipio(this.idMunicipio);

    this.getGestao();

    this.estatisticasService.getEstatisticaMunicipio(this.idMunicipio).subscribe(res => {
      this.valor_total_licitacoes = res.dados[0].valor_licitacoes
    })

  }

  ngAfterViewInit() {
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = '#F5F5F5';
  }

  get municipio() {
    return this.municipioService.municipio
  }

  get prefeito() {
    return this.candidatosService.candidato
  }

  getGestao() {
    let ano = new Date().getFullYear();
    this.municipioService.getGestao(this.idMunicipio, ano).subscribe(res => {
      this.gestao = res.dados[0];
      this.candidatosService.getCandidato(this.gestao.id_candidato);
    })
  }

}
