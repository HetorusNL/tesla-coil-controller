from time import sleep
import mido
from serial_handler import SerialHandler

sh = SerialHandler("COM4")
print(sh.open())

sh.write(b"\n")
sh.write(b"\n")
print(sh.read().decode("utf-8"))
sh.write(b"n")
sleep(0.1)
print(sh.read().decode("utf-8"))

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
sequence_number = 0
# enter midi mode
sh.write(bytearray([0x02, sequence_number, 0x01, 0x00, 0x03]))
sequence_number = (sequence_number + 1) % 256
sleep(0.25)
print(list(sh.read()))
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
            sequence_number,
            0x02,
            len(midi_msg),
            *midi_msg,
            0x03,
        ]
        sequence_number = (sequence_number + 1) % 256
        print("msg > ", new_midi_msg)
        sh.write(bytearray(new_midi_msg))
        response = list(sh.read())
        print(response)
# exit midi mode
sh.write(bytearray([0x02, sequence_number, 0x03, 0x00, 0x03]))
print("on", on, "off", off)
print(file.length)
print(cnt)
