#include <LiquidCrystal.h>
LiquidCrystal lcd(7,6,5,4,3,2);

void set(int a,int b){
   digitalWrite(a,b);
}
float g;
void setup(){
  pinMode(9,OUTPUT);
  pinMode(10,INPUT);
  lcd.begin(16,2);
}
void loop(){
  set(9,HIGH);
  delayMicroseconds(5);
  set(9,LOW);
  delayMicroseconds(5);
  g=(pulseIn(10,HIGH)*0.034)/2;
  lcd.setCursor(4,1);
  lcd.print(g);
}
