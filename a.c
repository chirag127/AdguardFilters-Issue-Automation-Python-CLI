#include<stdio.h>
#include<conio.h>

int proc,res,i,j,row=0,flag=0;
static int pro[3][3],req[3][3],st_req[3][3],st_pro[3][3];

void main()
{
 clrscr();

 printf("\nEnter the number of Processes:");
 scanf("%d",&proc);
 printf("\nEnter the number of Resources:");
 scanf("%d",&res);

 printf("\nEnter the Process Matrix:");
 for(i=0;i<proc;i++)
  for(j=0;j<res;j++)
	 scanf("%d",&pro[i][j]);

 printf("\nEnter the Request Matrix:");
 for(i=0;i<res;i++)
  for(j=0;j<proc;j++)
	 scanf("%d",&req[i][j]);

 row=0;
 while(!kbhit())
 {
  for(i=0;i<res;i++)
  {
   if(pro[row][i]==1)
	{
	 if(st_pro[row][i]>1 && flag==1)
	 {
	  printf("\nDeadlock Occured");
	  getch();
	  exit(0);
	 }
	 st_pro[row][i]++;
	 row=i;
	 break;
	}
  }

  for(i=0;i<proc;i++)
  {
   if(req[row][i]==1)
	{
	 if(st_req[row][i]>1)
	 {
	  printf("\nDeadlock Occured");
	  getch();
	  exit(0);
	 }
	 st_req[row][i]++;
	 row=i;
	 flag=1;
	 break;
	}
  }
 }
 cprintf("\nNo Deadlock Detected");
 getch();
 getch();
} 
