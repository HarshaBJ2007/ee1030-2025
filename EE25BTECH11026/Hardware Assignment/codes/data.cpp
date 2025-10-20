#include "Arduino.h"
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  lcd.setCursor(0,0);
  lcd.print("Digital");
  lcd.setCursor(0,1);
  lcd.print("Thermometer");
  delay(2000);
}

void loop() {
  const int numSamples = 5;
  long total = 0;

  for (int i = 0; i < numSamples; i++) {
    total += analogRead(A0);
    delay(100);  
  }

  float avgOutput = total / (float)numSamples;  
  float voltage = avgOutput * 5.0 / 1023.0;     
  float temperature = 281.69 * voltage - 771.66; //linear regression formula

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temperature:");
  lcd.setCursor(0,1);
  lcd.print(temperature, 2);
  lcd.print(" C");

  delay(1000);  
}
