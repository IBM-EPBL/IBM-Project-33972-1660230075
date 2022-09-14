# IBM-Project-33972-1660230075
Personal Assistance for Seniors Who Are Self-Reliant

// Code for the above Temperature and PIR sensor related project 
void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(12, OUTPUT);
}

void loop()
{
  int motion=digitalRead(2);
  double temperature=analogRead(A2);
  double detectedtemp=(((temperature/1024)*5)-0.5)*100;
  if(motion==1)
  {
    tone(12,400);
    delay(1000);
    noTone(12);
    delay(1000);
  }
  if(detectedtemp>60.00)
  {
    tone(12,300);
    delay(1000);
    noTone(12);
    delay(1000);
  }
}  
