import { Component, ElementRef, Input, OnChanges, ViewChild, ViewEncapsulation, HostListener } from '@angular/core';
import * as d3 from 'd3';
import d3Tip from 'd3-tip';
import { formatCurrency } from '@angular/common';

@Component({
  selector: 'app-barchart-empresas',
  encapsulation: ViewEncapsulation.None,
  templateUrl: './barchart-empresas.component.html',
  styleUrls: ['./barchart-empresas.component.css']
})
export class BarchartEmpresasComponent implements OnChanges {
  @ViewChild('chartEmpresas', {static: false}) 
  private chartContainer: ElementRef;
  
  rankingEmpresas: any;
  nomesEmpresas: string[];
  valoresLicitacoes: number[];

  @Input()
  dataEmpresas: any[];

  margin = {top: 20, right: 31, bottom: 20, left: 120};

  constructor() { }
  
  ngOnChanges(): void {
    if (!this.dataEmpresas) { return; }

    this.createChartEmpresas();
  }
  
  onResize() {
    this.createChartEmpresas();
  }

  private createChartEmpresas(): void {
    const element = this.chartContainer.nativeElement;
    const dataEmpresas = this.dataEmpresas;
    
    
    let realFormatter = (value) => {
      return formatCurrency(value, "pt-BR", "", "BRL", "1.0-0")
    }
    
    let height = dataEmpresas.length * 25 + this.margin.top + this.margin.bottom
    
    d3.select(element).select('svg').remove();
    
    const svg = d3.select(element).append('svg')
        .attr("viewBox", `0 0 670 290`);

    const contentWidth = element.offsetWidth - this.margin.left - this.margin.right;
    const contentHeight = element.offsetHeight - this.margin.top - this.margin.bottom;

    let x = d3.scaleLinear()
      .domain([0, d3.max(dataEmpresas, d => d.valor_licitacoes)])
      .range([this.margin.left, this.margin.left + contentWidth])

    let y = d3.scaleBand()
      .domain(dataEmpresas.map(d => d.nome_participante))
      .range([this.margin.top, this.margin.top + contentHeight])
      .padding(0.1)

    let xAxis = g => g
      .attr("transform", `translate(0, ${contentHeight + this.margin.top})`)
      .style("font", "12px sans-serif")
      .call(d3.axisBottom(x).ticks(contentWidth / 180)
        .tickFormat(function(d) { return realFormatter(d);}
        ).tickSizeOuter(0)
      )

    let yAxis = g => g
      .attr("transform", `translate(${this.margin.left}, 0)`)
      .call(d3.axisLeft(y).tickSizeOuter(0))

    const tip = d3Tip()

    tip
      .attr('class', 'd3-tip')
      .offset([-10, 0])
      .html(function(d) {
        return "<div><span>" + d.nome_participante + "</span></div>" +
               "<div><span style='color:white'>" + "R$"+ realFormatter(d.valor_licitacoes) + "</span></div>";
      });

    svg.call(tip);

    svg.append("g")
      .attr("fill", "steelblue")
      .selectAll("rect")
      .data(dataEmpresas)
      .join("rect")
      .attr("class", "bar")
      .attr("x", x(0))
      .attr("y", d => y(d.nome_participante))
      .attr("height", y.bandwidth())
      .on('mouseover', (d, i, n) => tip.show(d, n[i]))
      .on("mouseout", d => tip.hide(d));

    svg.append("g")
      .call(xAxis);

    svg.append("g")
      //.style("font", "10px sans-serif")
      .call(yAxis);

    svg.selectAll("rect")
      .data(dataEmpresas)
      .transition()
      .duration(2000)
      .attr("x", d => x(0))
      .attr("width", d => x(d.valor_licitacoes) - x(0));    

    let format = x.tickFormat(20)

    svg.append("g")
        .attr("fill", "#151C48")
        .style("font", "12px sans-serif")
      .selectAll("text")
      .data(dataEmpresas)
      .join("text")
        .attr("x", d => x(Number(d.valor_licitacoes)) - 4)
        .attr("y", d => y(d.nome_participante) + y.bandwidth() / 2)
        .attr("dy", "0.35em")
        .attr("dx", "10px")
        .text(d => format(Number(d.valor_licitacoes)));

    /*svg.append("g")
      .transition()
      .duration(900)
      .on("start", function repeat() {
        d3.active(this)
            .tween("text", function() {
              var that = d3.select(this),
                  i = d3.interpolateNumber(that.text().replace(/,/g, ""), data);
              return function(t) { that.text(format(i(t))); };
            })
          .transition()
            .delay(1500)
            .on("start", repeat);
      });*/
  }

}