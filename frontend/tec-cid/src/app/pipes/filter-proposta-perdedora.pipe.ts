import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filterPropostaPerdedora'
})
export class FilterPropostaPerdedoraPipe implements PipeTransform {

  transform(objects: any[]): any {
    if (objects) {
      return objects.filter(object => {
        return object.situacao_proposta === "Perdedora";
      });
    }
  }

}
