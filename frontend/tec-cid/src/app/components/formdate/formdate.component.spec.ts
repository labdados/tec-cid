import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FormdateComponent } from './formdate.component';

describe('FormdateComponent', () => {
  let component: FormdateComponent;
  let fixture: ComponentFixture<FormdateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FormdateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FormdateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
