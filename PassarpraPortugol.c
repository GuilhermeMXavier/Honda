#include <stdio.h>

int main(){

    int v1, v2, v3, blocos, c;

    blocos = 7;


    v1 = 3;
    v2 = 2;
    v3 = 3;



    for (c = 0; c < blocos; c++){
        
        if (c % 2 == 0){                         
        printf("Bloco 1 -> Torre %d\n", v1); 
        v1--;
        if (v1 == 0){
            v1 = 3;
        }
    }

        if ((c - 1) % 4 == 0){                  
        printf("Bloco 2 -> Torre %d\n", v2); 
        v2 = v2 + 1;                        
        if (v2 == 4){                      
             v2 = 1;
        }
    }


        if ((c + 5) % 8 == 0){                  
        printf("Bloco 3 -> Torre %d\n", v3);
        v3 = v3 - 1;
        if (v3 == 0){
            v3 = 3;
        }    
    }

}


}   