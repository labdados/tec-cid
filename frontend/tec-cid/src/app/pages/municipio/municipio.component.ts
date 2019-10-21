import { Component, OnInit } from '@angular/core';
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
export class MunicipioComponent implements OnInit {

  licitacoes: Licitacao[] = [];
  idMunicipio: any;
  ano: string = '';
  tipoLic: any = '';
  codTipoLic: string = '';
  gestao: Gestao = new Gestao(0, 0, '');
  valor_total_licitacoes: any = '';

  page: number = 1;
  prev: boolean = true;
  next: boolean;

  anos: any[] = ["2016", "2017", "2018", "2019", "Todos",]
  tipos: any[] = ["Concorrência", "Tomada de Preços", "Convite", "Concurso", "Leilão", "Dispensa por Valor", "Dispensa por outros motivos", "Inexigível", "Sem Licitação", "Pregão Eletrônico", "Pregão Presencial", "Adesão a Registro de Preço", "Chamada Pública", "RDC - Regime Diferenciado de Contratações Públicas", "Todas"]

  configAno = {
    displayKey: "Anos",
    placeholder: 'Selecione o ano',
    noResultsFound: 'Ano não encontrado',
  };

  configLic = {
    displayKey: "Tipos de Licitação",
    placeholder: 'Selecione o tipo de licitação',
    noResultsFound: 'Tipo não encontrado',
  };

  constructor(
    private route: ActivatedRoute,
    private municipioService: MunicipiosService,
    private candidatosService: CandidatosService,
    private estatisticasService: EstatisticasService,
    private router: Router
  ) { }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => this.idMunicipio = params['idMunicipio']);

    this.municipioService.getMunicipio(this.idMunicipio);

    this.getGestao();

    this.estatisticasService.getEstatisticaMunicipio(this.idMunicipio).subscribe(res => {
      this.valor_total_licitacoes = res.dados[0].valor_licitacoes
    })
  
    this.route.params
      .pipe(switchMap((params: Params) => this.loadMunicipio(+params.idMunicipio))).subscribe(res => {
        this.licitacoes = res.dados;
        console.log(this.licitacoes)
        if (this.licitacoes.length < 10) {
          this.next = true;
        }
      });
  }

  get municipio() {
    return this.municipioService.municipio
  }

  get prefeito() {
    return this.candidatosService.candidato
  }
  
  loadMunicipio(idMunicipio: any) {
    return this.municipioService.getLicitacoesMunicipio(idMunicipio, this.ano, this.tipoLic, this.page);
  }

  setAno() {
    // this.municipioService.getLicitacoesMunicipio(this.codUni, this.ano, this.codTipoLic, this.page).subscribe(res => {
    //   this.licitacoes = res.dados;
    // });
  }

  setTipoLicitacao() {
    if (this.tipoLic == "Concorrência") {
      this.codTipoLic = "1"
    } else if (this.tipoLic == "Tomada de Preços") {
      this.codTipoLic = "2"
    } else if (this.tipoLic == "Convite") {
      this.codTipoLic = "3"
    } else if (this.tipoLic == "Concurso") {
      this.codTipoLic = "4"
    } else if (this.tipoLic == "Leilão") {
      this.codTipoLic = "5"
    } else if (this.tipoLic == "Dispensa por Valor") {
      this.codTipoLic = "6"
    } else if (this.tipoLic == "Dispensa por outros motivos") {
      this.codTipoLic = "7"
    } else if (this.tipoLic == "Inexigível") {
      this.codTipoLic = "8"
    } else if (this.tipoLic == "Sem Licitação") {
      this.codTipoLic = "9"
    } else if (this.tipoLic == "Pregão Eletrônico") {
      this.codTipoLic = "10"
    } else if (this.tipoLic == "Pregão Presencial") {
      this.codTipoLic = "11"
    } else if (this.tipoLic == "Adesão a Registro de Preço") {
      this.codTipoLic = "12"
    } else if (this.tipoLic == "Chamada Pública") {
      this.codTipoLic = "13"
    } else if (this.tipoLic == "RDC - Regime Diferenciado de Contratações Públicas") {
      this.codTipoLic = "14"
    } else {
      this.codTipoLic = null
    }
    this.page = 1;
    this.prev = true;
    this.municipioService.getLicitacoesMunicipio(this.idMunicipio, this.ano, this.codTipoLic, this.page).subscribe(res => {
      this.verificacao(res.dados);
      this.licitacoes = res.dados;
    });

  }

  anterior() {
    this.next = false;
    this.page--;
    if (this.page != 1) {
      this.municipioService.getLicitacoesMunicipio(this.idMunicipio, this.ano, this.codTipoLic, this.page).subscribe(res => {
        this.licitacoes = res.dados;
      });
    } else {
      this.page = 1
      this.prev = true;
      this.municipioService.getLicitacoesMunicipio(this.idMunicipio, this.ano, this.codTipoLic, this.page).subscribe(res => {
        this.licitacoes = res.dados;
      });
    }
  }

  proximo() {
    this.page++
    this.prev = false;

    this.municipioService.getLicitacoesMunicipio(this.idMunicipio, this.ano, this.codTipoLic, this.page).subscribe(res => {
      this.verificacao(res.dados)     
          
      this.licitacoes = res.dados;
      
    });
  }

  verificacao(lista:any[]){
    if (lista.length < 10) {
      this.next = true;
    } else {
      this.next = false;
    }
  }

  exibirLicitacao(idLicitacao:any) {
    this.router.navigate([`/municipio/${this.idMunicipio}/licitacao/${idLicitacao}`])
  }

  getGestao() {
    let ano = new Date().getFullYear();
    this.municipioService.getGestao(this.idMunicipio, ano).subscribe(res => {
      this.gestao = res.dados[0];
      this.candidatosService.getCandidato(this.gestao.id_candidato);
    })
  }

}
