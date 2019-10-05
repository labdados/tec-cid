import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Licitacao } from 'src/app/models/licitacao.model';
import { LicitacaoService } from 'src/app/services/licitacao.service';

@Component({
  selector: 'app-licitacao',
  templateUrl: './licitacao.component.html',
  styleUrls: ['./licitacao.component.css']
})
export class LicitacaoComponent implements OnInit {

  codUni:string;
  idLicitacao: string;
  licitacao: Licitacao = null;

  constructor(
    private route: ActivatedRoute,
    private licitacaoService: LicitacaoService
  ) { }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.codUni = params['codUnidadeGest'];
      this.idLicitacao = params['idLicitacao'];

      this.licitacaoService.getLicitacao(this.idLicitacao).subscribe(res => {
        this.licitacao = res.dados[0];
      })

      this.licitacaoService.getPropostas(this.idLicitacao);
    });
  }

  get propostas() {
    return this.licitacaoService.propostas
  }

}
