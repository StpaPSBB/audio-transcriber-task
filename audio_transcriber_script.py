import os
import sys
import numpy as np
import whisper
import av

MODEL_NAME = "small"
LANG = "ru"
TARGET_SR = 16000

def extract_audio_to_numpy(video_path):
    container = av.open(video_path)
    if not container.streams.audio:
        raise ValueError("В файле нет аудиодорожки")

    audio_stream = container.streams.audio[0]
    resampler = av.AudioResampler(format="fltp", layout="mono", rate=TARGET_SR)

    frames = []
    for packet in container.demux(audio_stream):
        for frame in packet.decode():
            frames.extend(resampler.resample(frame))

    if not frames:
        raise ValueError("Аудиодорожка пуста или не декодируется")

    return np.concatenate([f.to_ndarray().flatten() for f in frames]).astype(np.float32)

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("Использование: python audio_recognizer.py <video.mp4> [output.txt]")
        return

    video_path = args[0]
    output_path = args[1] if len(args) > 1 else "transcript.txt"

    if not os.path.isfile(video_path):
        print("Видеофайл не найден.")
        return

    print("1/2: Извлечение аудио...")
    audio_data = extract_audio_to_numpy(video_path)

    print("2/2: Распознавание речи...")
    model = whisper.load_model(MODEL_NAME, device="cpu")
    result = model.transcribe(audio_data, language=LANG, fp16=False)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"].strip())

    print(f"Готово. Текст сохранён в {output_path}")

if __name__ == "__main__":
    main()
