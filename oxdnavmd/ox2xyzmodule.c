#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// let's do this with ctypes, as it seems way way easier.

int ox2xyz_run(char dat_FNAME[], 
               char top_FNAME[],
               char energy_FNAME[]) 
{
    FILE *fp_energy;
    fp_energy = fopen(energy_FNAME,"w");

    FILE *fp_top;
    fp_top = fopen(top_FNAME,"r");
    char buff[1000]; // buffer
    fscanf(fp_top, "%s", buff);
    fclose(fp_top);
    int Num_nts = atoi(buff);
    float DATA [9] ; 
    float STACK [3] ; 
    float BACK [3] ;
    FILE *fp_dat;
    fp_dat = fopen(dat_FNAME,"r");
    float BOX_SIZE = 0;
    while (fgets (buff, sizeof(buff), fp_dat)) {
        if (buff[0] == 't') {
            fprintf(fp_energy,"%d\n", Num_nts*2) ;
        }
        if (buff[0] == 'b') {
            fprintf(fp_energy,"#molecule\n");
            char * tmp_token = strtok(buff, " ");
            int i = 0;
            while (tmp_token != NULL) {
                if  (i == 2){
                    BOX_SIZE = atof(tmp_token);
                }
                tmp_token = strtok(NULL, " ");
                i ++;
            }  
        }
        if (buff[0] != 't' && buff[0] != 'b' && buff[0] != 'E') {
            char * token = strtok(buff, " ");
            int i = 0;
            while (token != NULL) {
                DATA[i] = atof(token) ; 
                token = strtok(NULL, " ");
                i ++ ;
            }
            for (int i=0; i < 3 ; i++){
                while (DATA[i] < 0){
                   DATA[i] = (DATA[i] + BOX_SIZE);
                }
            }
            // I should probably check this is correct
            for (int i=0; i < 3; i++) {
                STACK[i] = DATA[i] - 0.34 * DATA[i+3] + 0.3408 * DATA[i+6] ;   
                BACK[i]  = DATA[i] + 0.34 * DATA[i+3] ;   
            }
            // print to new file. 
            fprintf(fp_energy,"C %f %f %f\n", BACK[0], BACK[1], BACK[2]); 
            fprintf(fp_energy,"O %f %f %f\n", STACK[0], STACK[1], STACK[2]); 
        }
    } 
    fclose(fp_dat);

    return 0;
    }

int main(){
    return 0;
}


    
