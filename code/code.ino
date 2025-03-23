int x;
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) 
  {
    x = Serial.readString().toInt();
    Serial.print(x + 1);
  }
}
