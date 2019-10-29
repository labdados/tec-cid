import { Component, ElementRef, Input, OnChanges, ViewChild, ViewEncapsulation, HostListener } from '@angular/core';
import * as d3 from 'd3';
//import { DataModel } from 'src/app/models/data.model';
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

  margin = {top: 0, right: 0, bottom: 90, left: 138};

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
    const contentHeight = element.offsetHeight + this.margin.top + this.margin.bottom;

    const x = d3
      .scaleLinear()
      .rangeRound([contentHeight, 0])
      .domain([0, d3.max(data, d => Number(d.valor_licitacoes))]);

    const y = d3
    .scaleBand()
    .range([0, contentHeight])
    .padding(0.22)
    .domain(data.map(d => d.nome_municipio));

    const g = svg.append('g')
      .attr('transform', 'translate(' + this.margin.left + ',' + this.margin.top + ')');

    g.append('g')
      .style("font", "12px sans-serif")
      .attr('class', 'axis axis--x')
      .attr('transform', 'translate(0,' + contentHeight + ')')
      .call(d3.axisBottom(x));

    g.append('g')
        .style("font", "14px sans-serif")
      .attr('class', 'axis axis--y')
      .call(d3.axisLeft(y).ticks(10))
      .append('text')
      .attr('y', 6)
        .attr('dy', '4.91em')
        .attr('text-anchor', 'end');

    g.selectAll('.bar')
      .data(data)
      .enter().append('rect')
        .attr('class', 'bar')
        .attr('y', d => y(d.nome_municipio))
        .attr('x', d => x(d.valor_licitacoes))
        .attr('height', y.bandwidth())
        .attr('width', d => contentWidth - x(d.valor_licitacoes));
  }
}
