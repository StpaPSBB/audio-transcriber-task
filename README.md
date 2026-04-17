# audio-transcriber-task

## Установка зависимостей
```bash
  python -m venv venv
  source /venv/bin/activate #или для Windows: source \venv\scripts\activate 
  pip install -r requirements.txt
```

## Запуск скрипта
```bash
  python audio_transcriber_script.py /path/to/video-file /path/to/result-file
```

## Структура 
```
text-extractor-task/
├── audio_transcriber_script.py           # скрипт для транскрибации видео
├── video/                     # видео для обработки
├── result.txt                 # результат обработки
├── .gitignore
├── requirements.txt           # зависимости проекта
└── README.md
```