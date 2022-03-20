# shop prog
 Tillämpad Programmering (TIATILL00S)
Exempel README 2
Niclas Lund
3 feb.


# Tutorial to a Readme

Detta program är skrivet i python. Det är ett program där du simuleras till att gå in i en butik och ev. handla något/några produkter. 

## Teknologier/Språk

Språket som använts är bara python. Inget är importerat och hela programmet är skrivet rakt från pythons egna bibliotek.

## Hur det fungerar (Usage)

Programmet listar först upp alla produkter och dess priser i butiken genom att for-loopa genom en class tidigare skapad:
```
    for Item in items:
        print(Item.name, " ", Item.price)
```
Efter detta frågar den efter ens pengar och sätter in detta som variabeln "money". När man sedan påstår vad man vill köpa kollar programmet först igenom om påståendet finns med inom attributet "name" i klassen. Om den gör det kollar den sedan om pris-attributet till just denna produkt är mindre än "money", om den är det går det igenom och "you bought __" printas eftersom man produkten både finns med i listan och man har mer pengar än just denna produkt.:
```
    for Item in items:
        if(Item.name == buy):
            if(Item.price < money):
                print("You bought", buy, "!")
                money2 = money - Item.price  <------ (subtraherar priset av produkten från pengarna man hade och gör ut det til en ny variabel.)
```
Detta repeteras mer eller mindre tre gånger innan butiken "stänger".

## Installation

Programmet körs genom att öppna .py filen.
Installation sker via filöverföring.

## To do

Det kan vara nyttigt att få andra som läser om projektet att få veta vad du saknar just nu i programmet. Gör detta gärna genom en lista där färdiga saker strukits över.
Exempel:


    ~~Skapa lista för butik~~
    ~~Subtrahera pengar på varje köp~~
    ~~Göra det möjligt att handla fler än 1 gång(er). ~~
    Gör en forloop av programmet, aka man kan handla hur många gånger som helst innan ens pengar tar slut.
    Lägg till fler produkter i butiken. 
    Skapa ett kvitto när man är klarhandlad på vad man har köpt. 
    Skapa mer och djupare dialog mellan kunden och butiken. 

## Att bidra (Contribution)

Då bedömning ännu ej är gjord på uppgiften så tillåts inga pull requests. Så fort bedömning är gjord kommer detta tillåtas.  

Vid större förändringar önskar jag att en issue öppnas för diskussion om vad som ska förändras.

## Licens (License)

[MIT](https://choosealicense.com/licenses/mit/)
NL_README.md
Visar NL_README.md.