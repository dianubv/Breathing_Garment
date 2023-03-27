#include <Arduino.h>

void setup() {
    Serial.begin(9600);
    randomSeed(analogRead(A0)); // initialisation du générateur de nombres aléatoires
}

void loop() {
    int random_number = random(6000); // génère un nombre aléatoire entre 0 et 9
    Serial.println(random_number); // affiche le nombre aléatoire sur la console série
    delay(1000); // attend 1 seconde
}


/* 
// si on utilise un diviseur de tension normal (comme sur le PCB ou la carte à trous)
     // Vout = Vin * R2 / (R1 + R2)
void setup() {
  pinMode(A0, INPUT);
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // read the input on analog pin A0:
  int analogValue1 = analogRead(A0);
  delay(200); // wait to have a second value
  int analogValue2 = analogRead(A0);
  // faire la moyenne pour lisser
  int analogValue = (analogValue1+analogValue2)/2;
  // print 
  Serial.println(analogValue);
  delay(200);
} */