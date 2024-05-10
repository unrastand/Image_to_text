int r_en = 2;
int l_en = 3;
int r_pwm = 5;
int l_pwm = 6;

// Define pins for ultrasonic sensor
const int trigPin = 9; // Trigger pin of ultrasonic sensor
const int echoPin = 10; // Echo pin of ultrasonic sensor

void backward(){
  digitalWrite(r_en, HIGH);
  digitalWrite(l_en, HIGH);
  analogWrite(r_pwm, 255);
  analogWrite(l_pwm, 0);
  }
void forward(){
  digitalWrite(r_en, HIGH);
  digitalWrite(l_en, HIGH);
  analogWrite(r_pwm, 0);
  analogWrite(l_pwm, 255);
  }

void stopmotor(){    
  digitalWrite(r_en, HIGH);
  digitalWrite(l_en, HIGH);
  analogWrite(r_pwm, 0);
  analogWrite(l_pwm, 0);
  }

void setup()
{
  pinMode(r_en, OUTPUT);
  pinMode(l_en, OUTPUT);
  pinMode(r_pwm, OUTPUT);
  pinMode(l_pwm, OUTPUT);
  
   Serial.begin(9600); // Initialize serial communication
  pinMode(trigPin, OUTPUT); // Set trigger pin as output
  pinMode(echoPin, INPUT); // Set echo pin as input
}

void loop()
{
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
  //enable raspbery pi processs
  if(distance_cm <200){
    Serial.print(1);
  }

if(Serial.read()=="open"){
  // Move motors forward
  while(digitalRead(limitSwitch==0){
  forward();}
  stopmotor();
  delay(500); // Wait for half a second 
  //to add other motor after ir sensor
  
}
  while(digitalRead(limitSwitch2==0){
  backward();}  
  stopmotor();
  delay(500);
// Wait for half a second 
  //to add other motor after ir sensor
  
  }
