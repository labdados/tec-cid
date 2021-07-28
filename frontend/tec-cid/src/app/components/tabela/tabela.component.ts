import { Component, OnInit, ViewChild, AfterViewInit, Input, Injectable, Output, EventEmitter, SimpleChanges, OnChanges } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import {MatDatepickerInput, MatDatepickerModule} from '@angular/material/datepicker';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { Licitacao } from 'src/app/models/licitacao.model';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Params, ActivatedRoute, Router } from '@angular/router';
import { trigger, state, style, transition, animate } from '@angular/animations';
import { TOUCH_BUFFER_MS } from '@angular/cdk/a11y';
import {LicitacaoService} from '../../services/licitacao.service'
import {LicitacaoComponent } from '../../pages/licitacao/licitacao.component'
import {FormdateComponent} from '../formdate/formdate.component'
import { chdir } from 'process';
import { thresholdSturges } from 'd3';

@Component({
  selector: 'app-tabela',
  templateUrl: './tabela.component.html',
  styleUrls: ['./tabela.component.css'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({ height: '0px', minHeight: '0' })),
      state('expanded', style({ height: '*' })),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
@Injectable({
  providedIn: 'root'
})
export class TabelaComponent implements OnInit {

  displayedColumns: string[] = ['data_homologacao', 'nome_unidade_gestora', 'valor_licitado', 'acao', 'modalidade_de_licitação'];
  dataSource: MatTableDataSource<Licitacao>;
  expandedElement: Licitacao | null;
  resultsLength: number;
  filtroVisivel:boolean = true
  datas_arr:any = ['2017-01-01','2020-12-31']
  contador:number = 0  
  @Input()
  LicitacaoID: any;

  @Output()
  mudouValor = new EventEmitter()

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  constructor(
    private municipioService: MunicipiosService,
    private licitacaoService: LicitacaoService,
    private route: ActivatedRoute,
    private router: Router,
    private licitacaoComponent: LicitacaoComponent,
    private formdateComponent : FormdateComponent
  ) { }

  ngOnInit() {
    this.InsertDados()
  }

  InsertDados(){
    this.getDataLicitacoesMunicipio(this.municipio.id,1).subscribe(res=>{
      if(res.dados.length==0){
        alert("Não existem dados para esse intervalo de tempo")
      }else{
        this.dataSource = new MatTableDataSource (res.dados);
        this.resultsLength = res.dados.length;
        this.dataSource.sort = this.sort;
        this.dataSource.paginator = this.paginator;
      }
    })
  }
  
  getDataLicitacoesMunicipio(id:any,pagina:number){
    return this.municipioService.getLicitacoesMunicipio(this.municipio.id,pagina,this.datas_arr[0],this.datas_arr[1])
  }

  get municipio(){
    return this.municipioService.municipio;
  }

  get licitacao(){
    return this.licitacaoService.licitacao
  }

  reqLicitacao(id_da_licitacao){
     this.licitacaoService.getLicitacao(id_da_licitacao).subscribe(res=>{
        this.licitacaoService.licitacao = res.dados[0]
        this.mudouValor.emit(res.dados[0].id_licitacao)
     })
  }
  
  mostrarFiltro(){
    this.filtroVisivel = false
  }

  
  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();
    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
  
  dataObj(dia,mes,ano){
    return{
      dia: dia,
      mes: mes,
      ano: ano,
    }
  }

  convertData(str){
      
      let data_split = str.split(" ")
      let meses = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
      let dia = data_split[2]
      let ano = data_split[3]
      let mes;
      for(let i =0;i<meses.length;i++){
        if(data_split[1] == meses[i]){
          if(i<10){
            let cont = i+1
            mes = "0"+cont
          }else{
            mes = i+1
          }
        } 
      }
      let novaData = this.dataObj(dia,mes,ano)
      this.datas_arr[this.contador] = novaData
      if(this.contador<1){
        this.contador++
      }else if(this.contador==1){
        this.contador=0
      }

    
  }

  onMudou(evento){
    const datas = [evento.dataInicial.toString(),evento.dataFinal.toString()]
    this.filtroVisivel = !this.filtroVisivel

    for(let valor of datas){
       if(valor !== "" || valor !== " "){
         this.convertData(valor)
       }
    }
    this.InsertDados()
  }

  scroll(){
    
    let ElementScroll = document.getElementById("bgtabela")
    ElementScroll.scrollIntoView({behavior:"smooth"})
  }



}
