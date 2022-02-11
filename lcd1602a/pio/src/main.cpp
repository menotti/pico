#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal.h>

const int rs = 16, en = 17, d4 = 18, d5 = 19, d6 = 20, d7 = 21;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

byte pi[8] = {
 0b00000,
 0b00000,
 0b11111,
 0b01010,
 0b01010,
 0b01010, 
 0b01010,
 0b00000,
};

void setup()
{
  lcd.createChar(0, pi);
  lcd.begin(16, 2);
  lcd.print("Hello World!");
  lcd.setCursor(0, 1);
  lcd.print("Raspberry ");
  lcd.write(byte(0));
  lcd.print(" Pico");
}

void loop() {
}