   import paho.mqtt.client as mqtt

def ao_conectar(client, userdata, flags, rc):
    print("nos conectamos com o seguinte código de resultados {}".format(str(rc)))

def ao_receber(client, userdata, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))
