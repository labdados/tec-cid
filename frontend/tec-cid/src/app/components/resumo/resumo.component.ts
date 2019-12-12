import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-resumo',
  templateUrl: './resumo.component.html',
  styleUrls: ['./resumo.component.css']
})
export class ResumoComponent implements OnInit {

  @Input()
  dataEstatisticaMunicipio: any[];

  constructor() { }

  ngOnInit() {
  }

}
