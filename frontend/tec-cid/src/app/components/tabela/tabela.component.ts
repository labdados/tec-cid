import { Component, OnInit, ViewChild, AfterViewInit, Input, Injectable, Output, EventEmitter, SimpleChanges, OnChanges } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { Licitacao } from 'src/app/models/licitacao.model';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Params, ActivatedRoute, Router } from '@angular/router';
import { trigger, state, style, transition, animate } from '@angular/animations';
import { TOUCH_BUFFER_MS } from '@angular/cdk/a11y';
import {LicitacaoService} from '../../services/licitacao.service'
import {LicitacaoComponent } from '../../pages/licitacao/licitacao.component'

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

  displayedColumns: string[] = ['data_homologacao', 'nome_unidade_gestora', 'valor_licitado', 'acao'];
  dataSource: MatTableDataSource<Licitacao>;
  expandedElement: Licitacao | null;
  resultsLength: number;
  
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
    private licitacaoComponent: LicitacaoComponent
  ) { }

  ngOnInit() {
    this.InsertDados()
  }

  InsertDados(){
    this.getDataLicitacoesMunicipio(this.municipio.id,1).subscribe(res=>{
      this.dataSource = new MatTableDataSource (res.dados);
      this.resultsLength = res.dados.length;
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
  })
  }
  
  getDataLicitacoesMunicipio(id:any,pagina:number){
    return this.municipioService.getLicitacoesMunicipio(this.municipio.id,pagina)
  }

  get municipio(){
    return this.municipioService.municipio;
  }

  get licitacao(){
    return this.licitacaoService.licitacao
  }

  Reqlicitacao(param){
     this.licitacaoService.getLicitacao(param).subscribe(res=>{
        this.licitacaoService.licitacao = res.dados[0]
        this.mudouValor.emit(res.dados[0].id)
     })
  }
  

  
  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();
    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
  
  scroll(){
    
    let element = document.getElementById("bgtabela")
    element.scrollIntoView({behavior:"smooth"})
  }


}
