import { Component, ElementRef, Input, OnChanges, ViewChild, ViewEncapsulation, HostListener } from '@angular/core';
import * as d3 from 'd3';
import { DataModel } from 'src/app/models/data.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';

@Component({
  selector: 'app-bar-chart',
  encapsulation: ViewEncapsulation.None,
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.scss']
})
export class BarChartComponent implements OnChanges {
  @ViewChild('chart', {static: false}) 
  private chartContainer: ElementRef;
  
  rankingMunicipios: any;
  nomesMunicipios: string[];
  valoresLicitacoes: number[];

  @Input()
  data: any[];

  margin = {top: 20, right: 20, bottom: 30, left: 40};

  constructor(
    private estatisticasService: EstatisticasService
  ) {}

  ngOnChanges(): void {
    if (!this.data) { console.log("4", this.data); return; }
    console.log("3", this.data);
    this.createChart();
  }

  onResize() {
    this.createChart();
  }

  getRankingMunicipios() {
    this.rankingMunicipios = this.estatisticasService.getRankingMunicipios();
    // this.estatisticasService.getRankingMunicipios().subscribe(res => {
    //   this.rankingMunicipios = res.dados;
    //   console.log("1", this.rankingMunicipios);
    //   this.nomesMunicipios = res.dados.nome_municipio;
    //   this.valoresLicitacoes = res.dados.valor_licitacao;
    // })
  }

  private createChart(): void {
    d3.select('svg').remove();

    const element = this.chartContainer.nativeElement;
    //this.getRankingMunicipios();
    const data = this.data;
    console.log("2", data);
    

    const svg = d3.select(element).append('svg')
        .attr('width', element.offsetWidth)
        .attr('height', element.offsetHeight);

    const contentWidth = element.offsetWidth - this.margin.left - this.margin.right;
    const contentHeight = element.offsetHeight - this.margin.top - this.margin.bottom;

    const x = d3
      .scaleBand()
      .rangeRound([0, contentWidth])
      .padding(0.1)
      .domain(data.map(d => d.nome_municipio));

    const y = d3
      .scaleLinear()
      .rangeRound([contentHeight, 0])
      .domain([0, d3.max(data, d => Number(d.valor_licitacoes))]);

    const g = svg.append('g')
      .attr('transform', 'translate(' + this.margin.left + ',' + this.margin.top + ')');

    g.append('g')
      .attr('class', 'axis axis--x')
      .attr('transform', 'translate(0,' + contentHeight + ')')
      .call(d3.axisBottom(x));

    g.append('g')
      .attr('class', 'axis axis--y')
      .call(d3.axisLeft(y).ticks(10))
      .append('text')
        .attr('transform', 'rotate(-90)')
        .attr('y', 6)
        .attr('dy', '0.71em')
        .attr('text-anchor', 'end')
        .text('Frequency');

    g.selectAll('.bar')
      .data(data)
      .enter().append('rect')
        .attr('class', 'bar')
        .attr('x', d => x(d.nome_municipio))
        .attr('y', d => y(d.valor_licitacoes))
        .attr('width', x.bandwidth())
        .attr('height', d => contentHeight - y(d.valor_licitacoes));
  }
}
