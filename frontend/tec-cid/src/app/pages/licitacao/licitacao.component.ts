import { Component, OnInit, ElementRef, AfterViewInit, Injectable} from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { LicitacaoService } from '../../services/licitacao.service';
import { MunicipiosService } from '../../services/municipios.service';

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
  

  constructor(
    private route: ActivatedRoute,
    private licitacaoService: LicitacaoService,
    private municipioService: MunicipiosService,
    //private elementRef: ElementRef
  ) { }

  ngOnInit() {
    this.licitacaoService.getPropostas(this.licitacao.id_licitacao)
  }


  ngAfterViewInit() {
    //this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = '#F5F5F5';
  }

  get licitacao(){
    return this.licitacaoService.licitacao
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


  scroll(){
    let element = document.getElementById("superior")
    if(element == null) {
      setTimeout(() => {
        this.scroll()
      }, 1000);
    }
    else{
      element.scrollIntoView({behavior:"smooth"})
    }

  }
  
}
