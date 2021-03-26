#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#define MAX 100 

typedef struct SCanzone{
    int numero;
    char titolo[MAX];
    char artista[MAX];
    bool riproduzione;
}Canzone;

void memoria(Canzone* playlist, FILE *fp){       
    int i=0;
    char vett[MAX];
    const char *c=",";
    char *field;
    while(fgets(vett, MAX, fp)){        
        field=strtok(vett, c);

        playlist[i].numero=atoi(field);
        printf("numero: %d\n", playlist[i].numero);

        strcpy(playlist[i].titolo, strtok(NULL, c));
        printf("titolo: %s\n", playlist[i].titolo);

        strcpy(playlist[i].artista, strtok(NULL, c));

        playlist[i].artista[strlen(playlist[i].artista)-1]='\0';
        printf("artista: %s\n", playlist[i].artista);

        i++;
    }
}

void casuale(Canzone* playlist){            
    int k, n, w=0;
    srand(time(NULL));
    printf("\n");
    printf("In riproduzione\n");

    for(w=0;w<10;w++){
        playlist[w].riproduzione=false;
    }

    for(k=0;k<10;k++){
        do{
            n=rand()%10;
        }while(playlist[n].riproduzione==true);

        printf("titolo: %s, artista: %s\n", playlist[n].titolo, playlist[n].artista);
        playlist[n].riproduzione=true;
    }

}

int main(){
    int c, cont;
    int *play;
    FILE *fp;
    FILE *pf;
    pf=fopen("playlist.csv", "r");
    if(pf){
        for (c = getc(pf); c != EOF; c = getc(pf)){
        if (c == '\n')
        cont = cont + 1;
        }
    }
    
    fclose(pf);
    play = (Canzone *) malloc(sizeof(Canzone) * cont);
    fp=fopen("playlist.csv", "r");
    if (fp){
            printf("file ok!\n");
            Memorizzazione(playlist,fp);
            RiproduzioneCasuale(playlist);
            fclose(fp);
    }
    else {
        printf("Errore");
    }
    free(play);
    return 0;
    
}