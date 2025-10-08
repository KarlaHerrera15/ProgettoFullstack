import { Component, OnInit} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-firstten',
  standalone: true,
  imports: [],
  templateUrl: './firstten.component.html',
  styleUrl: './firstten.component.css'
})
export class FirsttenComponent {
 data!: Object; //Il ‘!’ serve a creare variabili non inizializzate
   loading: boolean=false;
   o! :Observable<Object>;
   constructor(public http: HttpClient) {}
   makeRequest(): void {
     console.log("here");
     this.loading = true;
     this.o = this.http.get('https://effective-goggles-v6pqq7qr6wwgfx9rj-5000.app.github.dev/first_ten_movies');
     this.o.subscribe(this.getData);
   }
   getData = (d : Object) =>
   {
     this.data = new Object(d);
     this.loading = false;
   }

   makeCompactRequest(): void {
     this.loading = true;
     this.http
       .get('https://effective-goggles-v6pqq7qr6wwgfx9rj-5000.app.github.dev/first_ten_movies')
       .subscribe(newData => {
       this.data = newData;
       this.loading = false;
       });
      }
}


