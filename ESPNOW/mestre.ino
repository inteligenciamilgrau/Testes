// neste programa o mestre ira enviar um dado hello world para o slave e fara o pareamento pelo MAC address

// EspnowController.ino

// a minimal program derived from
//          https://github.com/HarringayMakerSpace/ESP-Now

// This is the program that sends the data. (The Controller)

//=============

#include <ESP8266WiFi.h>
extern "C" {
    #include <espnow.h>
}

    // this is the MAC Address of the slave which receives the data
uint8_t remoteMac[] = {0x36, 0x33, 0x33, 0x33, 0x33, 0x33};

#define WIFI_CHANNEL 4

    // must match the slave struct
struct __attribute__((packed)) DataStruct {
    char text[32];
    unsigned long time;
};

DataStruct myData;

unsigned long lastSentMillis;
unsigned long sendIntervalMillis = 1000;
unsigned long sentMicros;
unsigned long ackMicros;

unsigned long lastBlinkMillis;
unsigned long fastBlinkMillis = 200;
unsigned long slowBlinkMillis = 700;
unsigned long blinkIntervalMillis = slowBlinkMillis;

byte ledPin = 14;


//==============

void setup() {
    Serial.begin(115200); Serial.println();
    Serial.println("Starting EspnowController.ino");

    WiFi.mode(WIFI_STA); // Station mode for esp-now controller
    WiFi.disconnect();

    Serial.printf("This mac: %s, ", WiFi.macAddress().c_str());
    Serial.printf("slave mac: %02x%02x%02x%02x%02x%02x", remoteMac[0], remoteMac[1], remoteMac[2], remoteMac[3], remoteMac[4], remoteMac[5]);

    Serial.printf(", channel: %i\n", WIFI_CHANNEL);

    if (esp_now_init() != 0) {
        Serial.println("*** ESP_Now init failed");
        while(true) {};
    }
    esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
    esp_now_add_peer(remoteMac, ESP_NOW_ROLE_SLAVE, WIFI_CHANNEL, NULL, 0);

    esp_now_register_send_cb(sendCallBackFunction);

    strcpy(myData.text, "Hello World");
    Serial.print("Message "); Serial.println(myData.text);

    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);

    Serial.println("Setup finished");

}

//==============

void loop() {
    sendData();
    blinkLed();
}

//==============

void sendData() {
    if (millis() - lastSentMillis >= sendIntervalMillis) {
        lastSentMillis += sendIntervalMillis;
        myData.time = millis();
        uint8_t bs[sizeof(myData)];
        memcpy(bs, &myData, sizeof(myData));
        sentMicros = micros();
        esp_now_send(NULL, bs, sizeof(myData)); // NULL means send to all peers
        Serial.println("sent data");
    }
}

//==============

void sendCallBackFunction(uint8_t* mac, uint8_t sendStatus) {
    ackMicros = micros();
    Serial.print("Trip micros "); Serial.println(ackMicros - sentMicros);
    Serial.printf("Send status = %i", sendStatus);
    Serial.println();
    Serial.println();
    if (sendStatus == 0) {
        blinkIntervalMillis = fastBlinkMillis;
    }
    else {
        blinkIntervalMillis = slowBlinkMillis;
    }
}

//================

void blinkLed() {
    if (millis() - lastBlinkMillis >= blinkIntervalMillis) {
        lastBlinkMillis += blinkIntervalMillis;
        digitalWrite(ledPin, ! digitalRead(ledPin));
    }
}
