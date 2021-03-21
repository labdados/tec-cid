import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
//import { DataModel } from 'src/app/models/data.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';
import {BarchartEmpresasComponent} from 'src/app/components/barchart-empresas/barchart-empresas.component'
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Municipio } from 'src/app/models/municipio.model';

@Component({
  selector: 'app-pesquisa',
  templateUrl: './pesquisa.component.html',
  styleUrls: ['./pesquisa.component.css']
})
export class PesquisaComponent implements OnInit {
  data: Observable<any>;
  dataEmpresas: Observable<any>;
  ExibirErrorEmpresa: boolean = false;
  ExibirErrorMunicipio: boolean = false;
  Loaded: boolean = true;
  ShowTabela:boolean = false;
  ShowLicitacao:boolean = false;
  barchartVisivel: boolean = true;
  MenuVisivel:boolean = false;
  NavVisivel:boolean = false;
  Principal:String = "carregando...";
  Inferior:String = "Licitações";
  constructor(
    private municipiosService: MunicipiosService,
    private estatisticasService: EstatisticasService
  ){}


  ExibeErrorTopEmpresasData(){
    this.ExibirErrorEmpresa = true
    }

  ExibeErrorMunicipiosData(){
    this.ExibirErrorMunicipio = true
    }

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
  }
  
  
  get municipio() {
    return this.municipiosService.municipio
  }

  MudaMunicipioBTN(){
    this.Principal = this.municipio.nome
  }

  troca(){
    this.Principal = this.Inferior
    this.Inferior = this.municipio.nome
  }
  troca2(){
    if(this.Inferior==this.Principal){
      this.Inferior = "Licitações"
      this.Principal = this.municipio.nome
    }
  }
  reset(){
    this.Inferior = "Licitações"
  }


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
  
 async InsertData(){
    await Promise.all([this.TopMunicipios(),this.TopEmpresas()]);

}

  ngOnInit() {
    this.InsertData()
  }

}

