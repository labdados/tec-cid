import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder, Validators, Form} from '@angular/forms'
@Component({
  selector: 'app-formdate',
  templateUrl: './formdate.component.html',
  styleUrls: ['./formdate.component.css']
})
export class FormdateComponent implements OnInit {
  public dataForm : FormGroup;
  public datas:Object
  constructor(
    public fb:FormBuilder
  ) { }

  ngOnInit():void {
      this.dataForm = this.fb.group({
        dataInicial:['',[Validators.required]],
        dataFinal:['',[Validators.required]]
      });
  }
  
  teste(){
    console.log(this.dataForm)
  }
  get DataForm(){
      this.datas = {dataInicial:this.dataForm.value.dataInicial,dataFinal:this.dataForm.value.dataFinal}
      return this.datas
  }
}