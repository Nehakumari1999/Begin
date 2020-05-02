

#include <stdio.h>

int main()

{ 

    int x,y;

    printf("Enter 1st no");

    scanf("%d",&x);

    printf("Enter 2nd no");

    scanf("%d",&y);

    printf("Value Before swapping in main is %d%d\n",x,y);

    x=x+y;

    y=x-y;
    x=x-y;

    printf("Value After swapping in main is %d%d",x,y);

    return 0;

}
