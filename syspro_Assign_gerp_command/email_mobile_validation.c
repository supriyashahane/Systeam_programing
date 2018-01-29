#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
main()
{
char email[100];
char s[50];
int i,j=0;
long long n;
int count = 0; 
printf("Email : ");
scanf("%s",&s);

for(i=0;email[i]!='\0';i++)
{
if(email[i]='@')
{
j=j+1;
}
}
if(j==1)
printf("valid");
else
printf("not valid");
printf("Enter an integer:" );
scanf("%12d",&n);
while(n != 0)
  {
    n /= 10;
    ++count;
  }
 printf("Number of digits: %d",count);
 if (count == 12)
   printf("valid number");
 else
   printf("not valid number");
     
} 


