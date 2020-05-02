



#include <stdio.h>

int finMax(int,int,int);
int finMax(int a,int z,int sign)
{   
    //Find Maximum
    return(a-(sign*z) );
}


int main()
{   
    int x,y,z,i,max;
    printf("Enter both nos ");
    scanf("%d%d",&x,&y);
    
    //Step1: Subtraction.
    z=x-y;
    //Step2:RightShift to get signed bit.Step3:Conversion of signed bit into 1 if it is -1, with bitwise and operator.
    
    i=(z>>31)&0x1;
    
   
    max=finMax(x,z,i);
    printf("Maximum no is%d\n", max);
    

    return 0;
}


