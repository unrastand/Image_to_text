#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

int r_en = 2;
int l_en = 3;
int r_pwm = 5;
int l_pwm = 6;
int limitSwitch = 7;
int limitSwitch2 = 8;
int buzzer = 9;

const int trigPin = 10;
const int echoPin = 11;

void backward() {
  digitalWrite(r_en, HIGH);
  digitalWrite(l_en, HIGH);
  analogWrite(r_pwm, 255);
  analogWrite(l_pwm, 0);
}

void forward() {
  digitalWrite(r_en, HIGH);
  digitalWrite(l_en, HIGH);
  analogWrite(r_pwm, 0);
  analogWrite(l_pwm, 255);
}

void stopmotor() {
  digitalWrite(r_en, LOW);
  digitalWrite(l_en, LOW);
}

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("SMART GATE");
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(r_en, OUTPUT);
  pinMode(l_en, OUTPUT);
  pinMode(r_pwm, OUTPUT);
  pinMode(l_pwm, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(limitSwitch, INPUT);
  pinMode(limitSwitch2, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  float distance_cm = duration * 0.0343 / 2;
 Serial.print(" ");
  if (distance_cm < 30) {
    Serial.println("1");
    delay(100);
  }  
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("SMART GATE");
    lcd.setCursor(0, 1);
    lcd.print("MOVE YOUR CAR CLOSER");
    digitalWrite(13,0);

  if (Serial.available() >0 ) {
    String command = Serial.readString();
    command.trim();
    if (command == "open") {
      digitalWrite(13,1);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("SMART GATE");
      lcd.setCursor(0, 1);
      lcd.print("LICENSE RECOGNISED");
      while (digitalRead(limitSwitch) == LOW) {
        digitalWrite(buzzer, HIGH);
        forward();
      }
      digitalWrite(buzzer, LOW);
      stopmotor();
      delay(500);
      while (digitalRead(limitSwitch2) == LOW) {
        digitalWrite(buzzer, HIGH);
        backward();
      }
      digitalWrite(buzzer, LOW);
      stopmotor();
    } else {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("SMART GATE");
      lcd.setCursor(0, 1);
      lcd.print("NOT RECOGNISED");
    }
  }
     digitalWrite(13,0);
}
