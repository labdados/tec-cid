import { Component, OnInit } from '@angular/core';
import { UnidadeGestora } from 'src/app/models/unidade-gestora.model';
import { ActivatedRoute, Params } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Licicatao } from 'src/app/models/licitacao.model';

@Component({
  selector: 'app-municipio',
  templateUrl: './municipio.component.html',
  styleUrls: ['./municipio.component.css']
})
export class MunicipioComponent implements OnInit {

  municipio: UnidadeGestora
  licitacoes: Licicatao[] = [];
  codUni: any;
  ano: string = '';
  tipoLic: any = '';
  codTipoLic: string = '';

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
  ) { }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => this.codUni = params['codUnidadeGest']);
    console.log(this.codUni);
    this.route.params
      .pipe(switchMap((params: Params) => this.loadMunicipio(+params.codUnidadeGest))).subscribe(res => {
        this.licitacoes = res.dados;
        if (this.licitacoes.length < 10) {
          this.next = true;
        }
      });
  }

  loadMunicipio(codUnidadeGest: any) {
    return this.municipioService.getLicitacoesMunicipio(codUnidadeGest, this.ano, this.tipoLic, this.page);
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
    this.municipioService.getLicitacoesMunicipio(this.codUni, this.ano, this.codTipoLic, this.page).subscribe(res => {
      this.verificacao(res.dados);
      this.licitacoes = res.dados;
    });

  }

  anterior() {
    this.next = false;
    this.page--;
    if (this.page != 1) {
      this.municipioService.getLicitacoesMunicipio(this.codUni, this.ano, this.codTipoLic, this.page).subscribe(res => {
        this.licitacoes = res.dados;
      });
    } else {
      this.page = 1
      this.prev = true;
      this.municipioService.getLicitacoesMunicipio(this.codUni, this.ano, this.codTipoLic, this.page).subscribe(res => {
        this.licitacoes = res.dados;
      });
    }
  }

  proximo() {
    this.page++
    this.prev = false;

    this.municipioService.getLicitacoesMunicipio(this.codUni, this.ano, this.codTipoLic, this.page).subscribe(res => {
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

}
