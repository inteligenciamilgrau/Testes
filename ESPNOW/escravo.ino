// escravo que recebe o dado vindo do ESP8266 usando protocoloca ESP NOW
// 1) ligar o monitor serial
// 2) ligar o mestre que ira enviar os dados
// 3) se tudo deu certo, os dados chegarao no monitor serial dizendo "hello world ...."

// EspnowSlave.ino

// a minimal program derived from
//          https://github.com/HarringayMakerSpace/ESP-Now

// This is the program that receives the data. (The Slave)

//=============

#include <ESP8266WiFi.h>
extern "C" {
    #include <espnow.h>
     #include <user_interface.h>
}

// it seems that the mac address needs to be set before setup() is called
//      and the inclusion of user_interface.h facilitates that
//      presumably there is a hidden call to the function initVariant()

/* Set a private Mac Address
 *  http://serverfault.com/questions/40712/what-range-of-mac-addresses-can-i-safely-use-for-my-virtual-machines
 * Note: by setting a specific MAC you can replace this slave ESP8266 device with a new one
 * and the new slave will still pick up the data from controllers which use that MAC
 */
uint8_t mac[] = {0x36, 0x33, 0x33, 0x33, 0x33, 0x33};

//==============

void initVariant() {
  WiFi.mode(WIFI_AP);
  wifi_set_macaddr(SOFTAP_IF, &mac[0]);
}

//==============

#define WIFI_CHANNEL 4

    // must match the controller struct
struct __attribute__((packed)) DataStruct {
    char text[32];
    unsigned int time;
};

DataStruct myData;

//============

void setup() {
    Serial.begin(115200); Serial.println();
    Serial.println("Starting EspnowSlave.ino");

    Serial.print("This node AP mac: "); Serial.println(WiFi.softAPmacAddress());
    Serial.print("This node STA mac: "); Serial.println(WiFi.macAddress());

    if (esp_now_init()!=0) {
        Serial.println("*** ESP_Now init failed");
        while(true) {};
    }

    esp_now_set_self_role(ESP_NOW_ROLE_SLAVE);

    esp_now_register_recv_cb(receiveCallBackFunction);


    Serial.println("End of setup - waiting for messages");
}

//============

void loop() {

}

//============

void receiveCallBackFunction(uint8_t *senderMac, uint8_t *incomingData, uint8_t len) {
    memcpy(&myData, incomingData, sizeof(myData));
    Serial.print("NewMsg ");
    Serial.print("MacAddr ");
    for (byte n = 0; n < 6; n++) {
        Serial.print (senderMac[n], HEX);
    }
    Serial.print("  MsgLen ");
    Serial.print(len);
    Serial.print("  Text ");
    Serial.print(myData.text);
    Serial.print("  Time ");
    Serial.print(myData.time);
    Serial.println();
}
