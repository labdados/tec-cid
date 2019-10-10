import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filterProposta'
})
export class FilterPropostaPipe implements PipeTransform {

  transform(objects: any[]): any {
    if (objects) {
      return objects.filter(object => {
        return object.situacao_proposta === "Vencedora";
      });
    }
  }

}
