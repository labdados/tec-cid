import { Component, OnInit, ViewChild, AfterViewInit, Input } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { Licitacao } from 'src/app/models/licitacao.model';
import { MunicipiosService } from 'src/app/services/municipios.service';
import { Params, ActivatedRoute, Router } from '@angular/router';


@Component({
  selector: 'app-tabela',
  templateUrl: './tabela.component.html',
  styleUrls: ['./tabela.component.css']
})
export class TabelaComponent implements OnInit {

  displayedColumns: string[] = ['data_homologacao', 'cd_ugestora', 'modalidade', 'valor_licitado'];
  dataSource: MatTableDataSource<Licitacao>;

  resultsLength: number;

  idMunicipio: any;

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: true }) sort: MatSort;

  constructor(
    private municipioService: MunicipiosService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => this.idMunicipio = params['idMunicipio']);

    this.municipioService.getLicitacoesMunicipio(this.idMunicipio, 1).subscribe(res => {
      this.dataSource = new MatTableDataSource(res.dados);
      this.resultsLength = res.dados.length;
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
    });

  }

  applyFilter(filterValue: string) {
    console.log(filterValue);
    this.dataSource.filter = filterValue.trim().toLowerCase();
    console.log(this.dataSource.data)

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  exibirLicitacao(idLicitacao: any) {
    this.router.navigate([`/municipio/${this.idMunicipio}/licitacao/${idLicitacao}`])
  }

}
