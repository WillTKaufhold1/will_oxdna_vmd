#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int ox2xyz_run(char dat_FNAME[], 
               char top_FNAME[],
               char traj_xyz[],
               char is_periodic[])
{

    FILE *fp_top;
    fp_top = fopen(top_FNAME,"r");
    char buff[1000]; // buffer
    fscanf(fp_top, "%s", buff);
    fclose(fp_top);

    FILE *fp_xyz;
    fp_xyz = fopen(traj_xyz, "w");

    int Num_nts = atoi(buff);
    float DATA [9] ; 
    float STACK [3] ; 
    float BACK [3] ;
    float a2 [3] ;
    FILE *fp_dat;
    fp_dat = fopen(dat_FNAME,"r");
    float BOX_SIZE = 0;
    while (fgets (buff, sizeof(buff), fp_dat)) {
        if (buff[0] == 't') {
            fprintf(fp_xyz,"%d\n", Num_nts*2) ;
        }
        if (buff[0] == 'b') {
            fprintf(fp_xyz,"#molecule\n");
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
            // the next bit is only needed if we have periodic boundary conditions... not for like DNA...
            if (is_periodic[0] == 'y'){  // shitty hack because not sure how to pass booleans
                for (int i=0; i < 3 ; i++){
                    while (DATA[i] < 0){

                       DATA[i] = (DATA[i] + BOX_SIZE);
                    }
                }
            }
           
            //okay, so apparently a2 is the cross product of a3 and a1, which we'll do manually
            //confusingly, in the oxdna code, a2 is given as the cross product of a3 and a1
            // 0 1 2 , 3 4 5 , 6 7 8
            a2[0] = DATA[7] * DATA[5] - DATA[8]*DATA[4];
            a2[1] = DATA[8] * DATA[3] - DATA[5]*DATA[6];
            a2[2] = DATA[6] * DATA[4] - DATA[7]*DATA[3];
            // implementation of cross product
            // I should probably check this is correct
            for (int i=0; i < 3; i++) {
                // check this!
                // this is wrong. because the axes are wrong.
                // fuck I don't even have a third axis here.
                STACK[i] = DATA[i] + 0.34 * DATA[i+3]  ;   
                // Note, the BACK needs to be along the third axis.
                // wait this is fucking wrong.
                
                BACK[i]  = DATA[i] - 0.34 * DATA[i+3] - 0.3408 * a2[i]  ; 
            }
            // print to new file. 
            fprintf(fp_xyz,"C %f %f %f\n", BACK[0], BACK[1], BACK[2]); 
            fprintf(fp_xyz,"O %f %f %f\n", STACK[0], STACK[1], STACK[2]); 
        }
    } 
    fclose(fp_dat);

    return 0;
    }

