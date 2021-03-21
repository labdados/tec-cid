import { Component, OnInit, ElementRef, AfterViewInit, Input, OnChanges, SimpleChanges } from '@angular/core';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Municipio } from 'src/app/models/municipio.model';
import { UnidadeGestoraService } from 'src/app/services/unidade-gestora.service';
import { EstatisticasService } from 'src/app/services/estatisticas.service';
import { Router } from '@angular/router';
import { Gestao } from 'src/app/models/gestao.model';
import {CandidatosService} from 'src/app/services/candidatos.service';
import {PesquisaComponent} from 'src/app/pages/pesquisa/pesquisa.component';
@Component({
  selector: 'app-filtros',
  templateUrl: './filtros.component.html',
  styleUrls: ['./filtros.component.css']
})
export class FiltrosComponent implements OnInit,OnChanges, AfterViewInit {
  Loader : boolean = false
  exibir: boolean = false;
  //instancia cidade usando a classe Municipio
  cidade: Municipio;
  valorLicitacoes: any;
  gestao: Gestao;
  ErroLoad: boolean = false
  @Input() NomeCidade:String = " "
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
    private elementRef: ElementRef,
    private Pesquisa: PesquisaComponent
  ) { }
  ngOnInit() {
    this.RecebeMunicipios()
  }

  ngOnChanges(changes: SimpleChanges){
      if(changes.NomeCidade.currentValue !==""){
        this.Pesquisa.MudaMunicipioBTN()
      }
  }
  RecebeMunicipios(){
    this.municipiosService.ReqMunicipios().subscribe(data=>{
      this.municipiosService.municipios = data.dados
    })
  }


  ngAfterViewInit() {
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = '#F5F5F5';
  }

  get municipios() {
    return this.municipiosService.municipios
  }

  /*
  get municipio() {
    return this.municipiosService.municipio
  }
  */

  get unidadesGestoras() {
    return this.unidadeGestoraService.unidadesGestoras
  }

  get candidato() {
    return this.candidatosService.candidato
  }
  /*
  displayFn(municipio?: Municipio): string | undefined {
    return municipio ? municipio.nome : undefined;
  }
*/

  filtroMunicipio() {
    if(this.cidade.id == undefined){
      //evita erro de selecionar algo que não existe
    }
    else{
      this.municipiosService.getMunicipio(this.cidade.id);
      this.getValorLicitacoes(this.cidade.id);
      this.ErroLoad = false
      this.GerenciaLoadBusca()
      this.Pesquisa.reset()
      this.unidadeGestoraService.getUnidadesGestorasByMunicipio(this.cidade.nome);
    }
  }

  getValorLicitacoes(id: string) {
    this.estatisticasService.getEstatisticaMunicipio(id).subscribe(res => {
      this.valorLicitacoes = res.dados[0].valor_licitacoes
    })
  }

  async getGestao() {
    //let ano = new Date().getFullYear();
    let ano = 2020
    const Espera = new Promise(resolve=>{
      this.municipiosService.getGestao(this.cidade.id,ano).subscribe(async res => {
          if(res.dados.length > 0){
            this.Pesquisa.barchartVisivel = false
            this.Pesquisa.Loaded = false
            this.Pesquisa.MenuVisivel = true
            this.Loader = false
            this.exibir = true
            this.Pesquisa.ShowTabela = true
            this.gestao = res.dados[0]
            return this.candidatosService.getCandidato(this.gestao.id_candidato);
          }
          else{
            this.Loader = false
           return this.ExibirErro()
          }
      })
    })
  }

  async GerenciaLoadBusca(){
      this.Loader = true
      this.exibir = false
      const retorno = await this.getGestao()
  }

  ExibirErro(){
    this.ErroLoad = true
  }
}
