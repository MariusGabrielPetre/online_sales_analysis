# Online Sales Analysis

## Descrierea proiectului
Acest proiect reprezintă un sistem de analiză pentru vânzările unui magazin online. Scopul proiectului este de a utiliza concepte avansate de Programare Orientată pe Obiecte (OOP) în Python și GitHub pentru gestionarea eficientă a versiunilor și colaborarea în echipă.

## Clasele și funcționalitățile

### Clasa `Product`
- **Atribute:**
  - `name`: Numele produsului.
  - `price`: Prețul produsului.
  - `quantity`: Cantitatea disponibilă în stoc.
- **Metode:**
  - `display_info`: Afișează informațiile produsului.
  - `update_quantity`: Actualizează cantitatea produsului.

### Clasa `ProductManager`
- **Atribute:**
  - `products`: Listă cu toate produsele disponibile.
- **Metode:**
  - `add_product`: Adaugă un produs în listă.
  - `display_products`: Afișează toate produsele disponibile.
  - `calculate_total_value`: Calculează valoarea totală a inventarului.
  - `remove_product`: Elimină un produs după nume.

### Clasa `Cart`
- **Atribute:**
  - `cart_items`: Lista de produse adăugate în coș.
- **Metode:**
  - `add_to_cart`: Adaugă produse în coș.
  - `calculate_total`: Calculează valoarea totală a coșului.
  - `display_cart`: Afișează conținutul coșului.

## Cum să rulezi proiectul
1. Clonează repozitoriul:
   ```bash
   git clone <URL-repozitoriu>
