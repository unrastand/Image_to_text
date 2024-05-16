#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

int r_en = 2;
int l_en = 3;
int r_pwm = 5;
int l_pwm = 6;
int limitSwitch = 7;
int limitSwitch2 = 8;
int buzzer = 9;
// Define pins for ultrasonic sensor
const int trigPin = 9;   // Trigger pin of ultrasonic sensor
const int echoPin = 10;  // Echo pin of ultrasonic sensor

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
  digitalWrite(r_en, HIGH);
  digitalWrite(l_en, HIGH);
  analogWrite(r_pwm, 0);
  analogWrite(l_pwm, 0);
}

void setup() {
  Serial.begin(9600);  // Initialize serial communication
  lcd.init();          // initialize the lcd
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("SMART GATE");
  pinMode(trigPin, OUTPUT);  // Set trigger pin as output
  pinMode(echoPin, INPUT);   // Set echo pin as input
  pinMode(r_en, OUTPUT);
  pinMode(l_en, OUTPUT);
  pinMode(r_pwm, OUTPUT);
  pinMode(l_pwm, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(limitSwitch, INPUT);
  pinMode(limitSwitch2, INPUT);
}

void loop() {
  // Clear the trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Send a 10 microsecond pulse to the trigger pin
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the duration of the pulse from the echo pin
  long duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters
  // Speed of sound is 343 meters/second or 0.0343 centimeters/microsecond
  // Distance = (duration / 2) * speed of sound
  float distance_cm = duration * 0.0343 / 2;

  //enable raspbery pi processs edit distance as you see fit
  if (distance_cm < 200) {
    Serial.print(1);
  } else {
    Serial.print(0);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("SMART GATE");
    lcd.setCursor(0, 1);
    lcd.print("MOVE YOUR CAR CLOSER");
  }

  if (Serial.read() == "open") {

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("SMART GATE");
    lcd.setCursor(0, 1);
    lcd.print("LICENSE RECOGNISED");
    // Move motors forward
    while(digitalRead(limitSwitch==0)){
      digitalWrite(buzzer, 1);
      forward();
    }
  digitalWrite(buzzer,0);
  stopmotor();
  delay(500); // Wait for half a second
    //to add other motor conditions after ir sensor if added
  } else {

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("SMART GATE");
    lcd.setCursor(0, 1);
    lcd.print("NOT RECOGNISED");
  }
  while(digitalRead(limitSwitch2==0)){
    digitalWrite(buzzer, 1);
    backward();
    }  
  stopmotor();
  digitalWrite(buzzer,0);
  delay(500);
  // Wait for half a second
  //to add other motor after ir sensor
}
