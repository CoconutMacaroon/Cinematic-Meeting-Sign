void setup() {
  Serial.begin(9600);     // Communication started with 9600 baud
  pinMode(2, OUTPUT);
  Serial.write("Hi!");
}
void loop() {
  char incomingByte = Serial.read(); // read the incoming byte:
  if (incomingByte == '1') {
    digitalWrite(2, HIGH);
  }
  if (incomingByte == '0') {
    digitalWrite(2, LOW);
  }
}
