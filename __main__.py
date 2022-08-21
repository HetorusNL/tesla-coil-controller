from time import sleep
import mido
from serial_handler import SerialHandler

sh = SerialHandler("COM3")
print(sh.open())
sleep(0.1)

# file = mido.MidiFile("bad-apple.mid")
# file = mido.MidiFile("Basshunter - DOTA 2.mid")
# file = mido.MidiFile("Basshunter - DOTA.mid")
# file = mido.MidiFile("pokemon-center.mid")
# file = mido.MidiFile("pokemon-center-2-.mid")
# file = mido.MidiFile("pokemon-center-3-.mid")
# file = mido.MidiFile("SAO - Crossing Field 2.mid")
# file = mido.MidiFile("SAO - Crossing Field.mid")
# file = mido.MidiFile("SAO - Swordland.mid")
file = mido.MidiFile("Touhou-Bad-Apple.mid")
cnt = 0
on = 0
off = 0
# enter midi mode
sh.write_msg([0x01, 0x00])
sleep(0.25)
print(sh.read_msg())
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
        new_midi_msg = [
            0x02,
            len(midi_msg),
            *midi_msg,
        ]
        print("msg > ", new_midi_msg)
        sh.write_msg(new_midi_msg)
        print(sh.read_msg())
# exit midi mode
sh.write_msg([0x03, 0x00])
print("on", on, "off", off)
print(file.length)
print(cnt)
