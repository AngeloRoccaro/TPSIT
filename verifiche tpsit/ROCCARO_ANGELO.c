#include<stdio.h>
#include<stdlib.h>
#define deck 52



typedef struct carta{                                                          //struct con le informazioni della carta
    int num;                                                                   //inizializzo la variabile num
    char seme;                                                                 //inizializzo la variabile seme
    Carta* next;
}Carta;

void enqueue (Carta **head, Carta **tail,  Carta *elemento){                    //comando per aggiungere dentro la coda
    if(is_empty(*head)){
        *head = elemento;
    }
    else{
        *tail->next = elemento;
    }
    *tail = elemento;
    elemento->next = NULL;

}

int main(){
    int main(int argc, char **argv){

    const char *seme[4] = {"Cuori", "Quadri", "Fiori", "Picche"};               //dichiaro e inizializzo il vettore dei semi
    const char *num[13] = {"Asso", "Due", "Tre", "Quattro", "Cinque",           //dichiaro e inizializzo il vettore delle facce
                            "Sei", "Sette", "Otto", "Nove", "Dieci",
                            "Jack", "Regina", "Re"};
}

Carta* dequeue(Carta **head,Carta **tail,Carta *elemento){                      //comando per togliere la coda
    Carta* ret = *head;
    if (is_empty(*head)){
        return NULL;
    }
        
    else{
        *head=ret->next  
    }
    if(*head == NULL){
        *tail = NULL;
    }
    
    return ret;
}

char setSeme(int cont){                                                         //in questo modo divido le carte del deck per i semi
    char seme;
    if(cont<13){
        seme = 'Cuori'
    }
    if(cont<26&& cont>13){
        seme = 'Fiori'
    }

    if(cont<39&& cont>26){
        seme = 'Quadri'
    }

    else{
        seme = 'Picche'
    }

}
