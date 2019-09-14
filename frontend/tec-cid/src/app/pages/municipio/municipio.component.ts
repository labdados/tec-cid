import { Component, OnInit } from '@angular/core';
import { UnidadeGestora } from 'src/app/models/unidade-gestora.model';
import { ActivatedRoute, Params } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { MunicipiosService } from 'src/app/services/municipios.service';

@Component({
  selector: 'app-municipio',
  templateUrl: './municipio.component.html',
  styleUrls: ['./municipio.component.css']
})
export class MunicipioComponent implements OnInit {

  municipio: UnidadeGestora
  licitacoes: any;

  constructor(
    private route: ActivatedRoute,
    private municipioService: MunicipiosService
  ) { }

  ngOnInit() {
    this.route.params
      .pipe(switchMap((params: Params) => this.loadMunicipio(+params.codUnidadeGest))).subscribe(res => {
        this.licitacoes = res.dados;
        // for (let i; i<this.licitacoes.dados)
        console.log(this.licitacoes)
      });
  }

  loadMunicipio(codUnidadeGest:any){
    return this.municipioService.getLicitacoesMunicipio(codUnidadeGest);

  }

}
