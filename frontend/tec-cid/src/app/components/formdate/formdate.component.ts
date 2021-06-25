import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import {FormGroup, FormBuilder, Validators, Form} from '@angular/forms'
@Component({
  selector: 'app-formdate',
  templateUrl: './formdate.component.html',
  styleUrls: ['./formdate.component.css']
})
export class FormdateComponent implements OnInit {
  public dataForm : FormGroup;
  public datas:Object
  @Output() mudouValor = new EventEmitter()
  

  constructor(
    public fb:FormBuilder
  ) { }

  ngOnInit():void {
      this.dataForm = this.fb.group({
        dataInicial:['',[Validators.required]],
        dataFinal:['',[Validators.required]]
      });
  }
  
  Emite(){
    this.mudouValor.emit(this.DataForm)
  }
  
  get DataForm():any{
      this.datas = {dataInicial:this.dataForm.value.dataInicial,dataFinal:this.dataForm.value.dataFinal}
      return this.datas
  }
}