import { Component, OnInit, ElementRef, AfterViewInit, Injectable} from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Licitacao } from 'src/app/models/licitacao.model';
import { LicitacaoService } from 'src/app/services/licitacao.service';
import { MunicipiosService } from 'src/app/services/municipios.service';

@Component({
  selector: 'app-licitacao',
  templateUrl: './licitacao.component.html',
  styleUrls: ['./licitacao.component.css']
})
@Injectable({
  providedIn: 'root'
})
export class LicitacaoComponent implements OnInit, AfterViewInit {

  idMunicipio:string;
  idLicitacao: string;
  licitacao: Licitacao = new Licitacao('', '', '', '', '', '', '', '', '', '', '', '', '','', '');

  constructor(
    private route: ActivatedRoute,
    private licitacaoService: LicitacaoService,
    private municipioService: MunicipiosService,
    private elementRef: ElementRef
  ) { }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.idMunicipio = params['idMunicipio'];
      this.idLicitacao = params['idLicitacao'];

      this.municipioService.getMunicipio(this.idMunicipio);

      this.licitacaoService.getLicitacao(this.idLicitacao).subscribe(res => {
        this.licitacao = res.dados[0];
      })

      this.licitacaoService.getPropostas(this.idLicitacao);
    });

  }

  ngAfterViewInit() {
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = '#F5F5F5';
  }

  get propostas() {
    return this.licitacaoService.propostas
  }

  get municipio() {
    return this.municipioService.municipio
  }

  get vencedores() {
    return this.licitacaoService.vencedores
  }

  get perdedores() {
    return this.licitacaoService.perdedores
  }

  get exibirPerdedor() {
    return this.licitacaoService.exibirPerdedores
  }

  scroll(){
    let element = document.getElementById("superior")
    element.scrollIntoView()
  }
  

}
