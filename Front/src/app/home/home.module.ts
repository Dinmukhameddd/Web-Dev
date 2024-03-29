import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';
import { ProductsComponent } from './products/products.component';
import { CategoriesComponent } from './categories/categories.component';
import { CategoryComponent } from './category/category.component';
import { ProductComponent } from './product/product.component';
import { CorzinaComponent } from './corzina/corzina.component';
import { OrderComponent } from './order/order.component';
import { FooterComponent } from './footer/footer.component';


@NgModule({
  declarations: [
    HomeComponent,
    HeaderComponent,
    ProductsComponent,
    CategoriesComponent,
    CategoryComponent,
    ProductComponent,
    CorzinaComponent,
    OrderComponent,
    FooterComponent,

  ],
    exports: [
        HeaderComponent,
        HomeComponent,
        FooterComponent
    ],
  imports: [
    CommonModule,
    HomeRoutingModule
  ]
})
export class HomeModule { }
