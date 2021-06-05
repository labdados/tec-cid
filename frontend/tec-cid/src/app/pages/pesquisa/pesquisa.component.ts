import { Component, HostListener, Input, OnChanges, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
//import { DataModel } from 'src/app/models/data.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';
import {BarchartEmpresasComponent} from 'src/app/components/barchart-empresas/barchart-empresas.component'
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Municipio } from 'src/app/models/municipio.model';
import { TabelaComponent } from '../../components/tabela/tabela.component';
import {LicitacaoComponent } from '../../pages/licitacao/licitacao.component'



@Component({
  selector: 'app-pesquisa',
  templateUrl: './pesquisa.component.html',
  styleUrls: ['./pesquisa.component.css']
})
export class PesquisaComponent implements OnInit, OnChanges {
  data: Observable<any>;
  dataEmpresas: Observable<any>;
  idMunicipio: Observable<any>;
  ExibirErrorEmpresa: boolean = false;
  ExibirErrorMunicipio: boolean = false;
  Loaded: boolean = true;
  ShowTabela:boolean = false;
  ShowLicitacao:boolean = false;
  MenuVisivel:boolean = false;
  Principal:String = "carregando...";
  Inferior:String = "Licitações";
  InferiorVisivel:Boolean = false;
  NavVisivel:Boolean = false;
  LicitacaoID:any;
  BtnLicitaVisibilidade: boolean = false;
  Starter:boolean = true
  LoadingData:boolean = true;
  visivelBarchat:boolean = true;
  loaderTabela:boolean = false;


  constructor(
    private municipiosService: MunicipiosService,
    private estatisticasService: EstatisticasService,
    private Tabela: TabelaComponent,
    private licitacaoComponet: LicitacaoComponent,
    ){}

  @HostListener('window:scroll', ['$event']) // for window scroll events
  onScroll(event) {
    if(window.scrollY > 280){
      this.NavVisivel = true
    }
    else{
      this.NavVisivel = false
      
    }
    }
  ExibeErrorTopEmpresasData(){
    this.ExibirErrorEmpresa = true
    }

  ExibeErrorMunicipiosData(){
    this.ExibirErrorMunicipio = true
    }
   
  ResetPagina(){
    this.ShowTabela = false
    this.ShowLicitacao = false
  }
  private ScrollParaLicitacao(){
    this.licitacaoComponet.scroll()
  }
  private ScrollParaTabela(){
    this.Tabela.scroll()
  }  
  private ScrollParaTop(){
    //
  }

  get DataMunicipios(){
    return this.estatisticasService.getDataMunicipios(10).subscribe(res=>{
      if(res.dados.length >0 ){
        this.LoadingData = false;
        this.data = res.dados
      }
    })
  }

  get DataEmpresas(){
    return this.estatisticasService.getDataEmpresas(10).subscribe(res=>{
      if(res.dados.length >0){
        this.dataEmpresas = res.dados
      }
      else{
        return this.ExibeErrorTopEmpresasData()
      }
    })
  }

  /*
  async TopMunicipios(){
    const RetornoMunicipios =new Promise(resolve=>{
        this.estatisticasService.getRankingMunicipios(10).subscribe(res =>{
          if(res.dados.length > 0){
            this.Loaded = false
            return this.data = res.dados;
          }
          else{
            return this.ExibeErrorMunicipiosData()
          }
        })
    })
    return RetornoMunicipios
  }*/
  
  
  get municipio() {
    return this.municipiosService.municipio
  }


  MudaMunicipioBTN(){
    this.Principal = this.municipio.nome
  }
  public ResetMenu(){
    this.Inferior = "Licitações"
    this.BtnLicitaVisibilidade = false
  }

  public SelectSuperior(){
    this.InferiorVisivel = !this.InferiorVisivel
  }
  public SelectInferior(){
    if(this.Inferior !== this.municipio.nome){
      this.Principal = "Licitações"
      this.Inferior = this.municipio.nome
      this.Tabela.scroll()
      
    }
    else if(this.Inferior == this.municipio.nome){
      this.Principal = this.municipio.nome;
      this.Inferior = "Licitações"
    }
  
  }

  public MenuAdd(){
    this.BtnLicitaVisibilidade = true
  }

/*
 async TopEmpresas(){
    const RetornoEmpresas = new Promise(resolve=>{
        this.estatisticasService.getRankingEmpresas(10).subscribe(async res =>{
          if(res.dados.length > 0){ 
            this.dataEmpresas = res.dados
             
          }
          else{
            return this.ExibeErrorTopEmpresasData()
          }
        })
    })
    return RetornoEmpresas
  }
  */
/*
 async InsertData(){
    await Promise.all([this.TopMunicipios(),this.TopEmpresas()]);

}*/

  onMudouValor(evento){
      this.LicitacaoID = "Licitação " + evento
      this.ShowLicitacao = true
      this.MenuAdd()
      this.licitacaoComponet.scroll()
  }
  ngOnInit() {
    this.DataEmpresas;
    this.DataMunicipios;
  
  }
  ngOnChanges(){
  }

}

