import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FirsttenComponent } from './firstten.component';
import { describe, beforeEach, it } from 'node:test';

describe('FirsttenComponent', () => {
  let component: FirsttenComponent;
  let fixture: ComponentFixture<FirsttenComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FirsttenComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FirsttenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
