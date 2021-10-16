unsigned short led[]    = {2,3,4,5,6,7};
unsigned short button[] = {8,9,10};
unsigned short count    = 1;
unsigned short i        = 0;

void setup() {
  
  for(i=0;i<6;i++)
    pinMode(led[i],OUTPUT);
  for(i=0;i<3;i++)
    pinMode(button[i],OUTPUT);
    
  for(i=0;i<3;i++)
    digitalWrite(button[i],LOW);
    
  for(i=0;i<3;i++)
    pinMode(button[i],INPUT);
    
  for(i=0;i<6;i++)
    digitalWrite(led[i],LOW);
    
}

void fun1(){
    for(i=0;i<6;i++)
        (i<2) ? (digitalWrite(led[i], HIGH)) : (digitalWrite(led[i], LOW));
    delay(2000);
    for(i=0;i<6;i++)
        digitalWrite(led[i],LOW);
    delay(2000);
}

void fun2(){
    for(i=0;i<6;i++)
        (i==2) ? (digitalWrite(led[i], HIGH)) : (digitalWrite(led[i], LOW));
    delay(1000);
    for(i=0;i<6;i++)
        (i==3) ? (digitalWrite(led[i], HIGH)) : (digitalWrite(led[i], LOW));
    delay(1000);
}

void fun3(){
    for(i=0;i<6;i++)
        digitalWrite(led[i],LOW);
    delay(1000);
    for(i=0;i<6;i++){
        (i>3) ? (digitalWrite(led[i], HIGH)) : (digitalWrite(led[i], LOW));
    }
    delay(1000);
}

void loop()
{
  if( digitalRead(button[0]) == LOW)
  {
        count = 0;
        while(count!=5)
        { 
            count++;   
            fun1();
        }
   }
   else if( digitalRead(button[1]) == LOW)
   {
        count = 0;
        while(count!=5)
        {
            count++;
            fun2();
        }    
   }
   else if( digitalRead(button[2])== LOW)
   {
        count = 0;
        while(count!=10)
        {
            count++;
            fun3();
        }
   }
   for(i=0;i<6;i++)
       digitalWrite(led[i],LOW);
}
