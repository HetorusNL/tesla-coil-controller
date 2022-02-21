from time import sleep
import mido
from serial_handler import SerialHandler

sh = SerialHandler("COM4")
print(sh.open())

sh.write(b"\n")
sh.write(b"\n")
print("1", sh.read().decode("utf-8"))
sh.write(b"y")
sleep(0.25)
print("2", sh.read().decode("utf-8"))
sh.write(b"330\n")
sleep(0.25)
print("3", sh.read().decode("utf-8"))
sh.write(b"n")
sleep(0.25)
print("4", sh.read().decode("utf-8"))
sh.write(b"\n")
print("5", sh.read().decode("utf-8"))

# file = mido.MidiFile("Basshunter - DOTA 2.mid")
file = mido.MidiFile("Basshunter - DOTA.mid")
# file = mido.MidiFile("pokemon-center.mid")
# file = mido.MidiFile("pokemon-center-2-.mid")
# file = mido.MidiFile("pokemon-center-3-.mid")
# file = mido.MidiFile("SAO - Crossing Field 2.mid")
# file = mido.MidiFile("SAO - Crossing Field.mid")
# file = mido.MidiFile("SAO - Swordland.mid")
cnt = 0
on = 0
off = 0
sh.write(b"m\n")  # enter midi mode
sleep(0.25)
print(sh.read().decode("utf-8"))
for msg in file:
    print(msg)
    if msg.type == "note_on":
        on += 1
    if msg.type == "note_off":
        off += 1
    if msg.type in ["note_on", "note_off"]:
        time = int(msg.time * 1000)
        midi_msg = [*msg.bytes(), int(time / 256), int(time % 256)]
        if msg.time:
            sleep(msg.time)
        if msg.channel in [0, 1, 2]:
            sh.write(bytearray(midi_msg))
            sh.write(b"\n")
        print(sh.read().decode("utf-8"))
sh.write(bytearray([0xFF]))  # exit midi mode
sh.write(b"\n")
print("on", on, "off", off)
print(file.length)
print(cnt)
