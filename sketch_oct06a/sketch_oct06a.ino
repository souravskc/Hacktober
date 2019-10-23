int s1=A0;
int k=500;
int s2=A1;
int M11=2;
int M10=4;
int M21=12;
int M20=13;
void setup() {
  // put your setup code here, to run once:
  pinMode(s1,INPUT);
  pinMode(s2,INPUT);
  pinMode(M11,OUTPUT);
  pinMode(M10,OUTPUT);
  pinMode(M21,OUTPUT);
  pinMode(M20,OUTPUT);
}

void forward()
{
  analogWrite(M11,255);
  analogWrite(M10,0);
  analogWrite(M21,255);
  analogWrite(M20,0);
}
void sttop()
{
  analogWrite(M11,0);
  analogWrite(M10,0);
  analogWrite(M21,0);
  analogWrite(M20,0);
}
void left()
{
  analogWrite(M11,180);
  analogWrite(M10,0);
  analogWrite(M21,0);
  analogWrite(M20,90);
}
void right()
{
  analogWrite(M11,0);
  analogWrite(M10,90);
  analogWrite(M21,180);
  analogWrite(M20,0);
}
void loop() {
  // put your main code here, to run repeatedly:
 
 if((analogRead(s1)<=k)&&(analogRead(s2)<=k))
 {  forward();}
 
 else if((analogRead(s1)>=k)&&(analogRead(s2)<=k))
{
  left();
}

else if((analogRead(s1)<=k)&&(analogRead(s2)>=k))
{
  right();
}

else if((analogRead(s1)<=k)&&(analogRead(s2)<=k))  
{ sttop();
  }

}
